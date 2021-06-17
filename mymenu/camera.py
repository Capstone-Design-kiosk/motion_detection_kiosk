import mediapipe as mp
import cv2
import numpy as np
import os
import pyautogui,autopy
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse

from .models import Menu
from .models import Order
from .models import OrderList
import webbrowser
from .views import menu_list_beverage
import time
import math
from matplotlib import pyplot as plt
from requests import request

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
folderPath = "FingerImages" #손가락 번호 이미지
myList = os.listdir(folderPath)
tipIds = [4, 8, 12, 16, 20]#손가락 5개 번호
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)


trynum=0#프로그램 실행시 처음 사용자인지 여부 확인용
try:
    latestnum = OrderList.objects.latest('order_num')#가장 최신 주문번호
    latestnum2=hash(latestnum.order_num)+1
except OrderList.DoesNotExist:#맨처음 프로그램 실행시 order내용이 아예 없을 때
    latestnum2=1
newnum = latestnum2 + 1  # 결제하기 누르고 다음 사람을 위해 이어지는 주문번호
class CAMERA(object):
    def urlconnect(request): #################페이지 전환
        print("들어옹냐")
        request = HttpRequest()
        response = menu_list_beverage(request)
        # html = response.content.decode('utf8')
        # print(response)
        # redirect_to = reverse('menu_list_beverage')
        # return HttpResponseRedirect(redirect_to)
        # print(Paginator.previous_page_number() )
        # webbrowser.open('http://127.0.0.1:8000/mymenu/menu_list/?page=Paginator.number|add:+1')
    def __init__(self):
        cap = cv2.VideoCapture(0)
        active = 0
        mode = ''
        def draw_finger_angles(image, results, joint_list): #손가락 각도

            # Loop through hands
            for hand in results.multi_hand_landmarks:
                # Loop through joint sets
                for joint in joint_list:
                    a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])  # 8 x,y좌표
                    b = np.array([hand.landmark[joint[1]].x, hand.landmark[joint[1]].y])  # 5 x,y좌표
                    c = np.array([hand.landmark[joint[2]].x, hand.landmark[joint[2]].y])  # 12 x,y좌표
                    d = np.array([hand.landmark[joint[3]].x, hand.landmark[joint[3]].y])  # 9 x,y좌표

                    radians = np.arctan2(d[1] - c[1], d[0] - c[0])-np.arctan2(b[1] - a[1], b[0] - a[0])
                    global angle
                    angle = np.abs(radians * 180.0 / np.pi) #2,3번째 손가락 각도

                    if angle > 180.0:
                        angle = 360 - angle 

                    cv2.putText(image, str(round(angle, 2)), tuple(np.multiply(b, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA) #각도 표시
            return image

        joint_list = [[8,5,12,9]] #2,3손가락
        with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
            while cap.isOpened():
                ret, frame = cap.read()
                # BGR 2 RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #좌우반전
                image = cv2.flip(image, 1)
                # Set flag
                image.flags.writeable = False
                # Detections
                results = hands.process(image)
                # Set flag to true
                image.flags.writeable = True
                # RGB 2 BGR
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
#########################################   손가락개수   #########################################
                if results.multi_hand_landmarks:
                    xList = [] #x좌표
                    yList = [] #y좌표
                    lmList = [] #id,x,y좌표
                    for num, hand in enumerate(results.multi_hand_landmarks):
                        mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                                  mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                                  mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                                  )
                        for id, lm in enumerate(hand.landmark):
                            h,w,c=image.shape
                            cx,cy=int(lm.x*w),int(lm.y*h)
                            xList.append(cx)
                            yList.append(cy)
                            # print(id, cx, cy)
                            lmList.append([id, cx, cy])
                            if id==8: #2번쨰 손가락이면
                                cv2.circle(image,(cx,cy),15,(255,0,255),cv2.FILLED) #원으로 표시
                                print(cx,cy)  #손가락 x,y좌표
                    if len(lmList) != 0:
                        fingers = []
                        # 엄지
                        if lmList[tipIds[0]][1] > lmList[tipIds[0 - 1]][1]: #오른손
                            if lmList[tipIds[0]][1] >= lmList[tipIds[0] - 1][1]:
                                fingers.append(1)
                            else:
                                fingers.append(0)
                        elif lmList[tipIds[0]][1] < lmList[tipIds[0 - 1]][1]: #왼손
                            if lmList[tipIds[0]][1] <= lmList[tipIds[0] - 1][1]:
                                fingers.append(1)
                            else:
                                fingers.append(0)


                        # 손가락 네개
                        for id in range(1, 5):
                            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                                fingers.append(1)

                            else:
                                fingers.append(0)

                        totalFingers = fingers.count(1)
                        print(totalFingers) #숫자 출력
                        cv2.putText(image, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                                    10, (255, 0, 0), 25)
                        draw_finger_angles(image, results, joint_list) #각도 측정(스와이프)
                        # h, w, c = overlayList[totalFingers].shape#손가락 화면에 넣고 싶었지만 이미지 크기 오류 발생
                        # print(h, w, c)
                        # image[0:h, 0:w] = overlayList[totalFingers - 1]
                        # cv2.rectangle(image, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
                        # if fingers[1] == 1 and fingers[2] == 0:
######################################손가락 위치 변환#########################################

                        if (fingers == [0, 1, 1, 0, 0]) & (active == 0) & (angle <5): #2,3 붙이면 스와이프모드 전환
                            mode = 'swipe'
                            active = 1
                        elif (fingers == [0, 1, 1, 0, 0]) & (active == 1) & (angle > 10): #2,3 스와이프 떨어뜨리면 다시 숫자모드로 전환
                            active = 0
                            mode = 'N'
                        if(mode == 'swipe') &(active == 1):
                            cv2.rectangle(image, (30, 20), (620, 470), (255, 255, 255), 3)
                            print("swipe")
                            if len(lmList) != 0:
                                if fingers[-1] == 1:
                                    active = 0
                                    mode = 'N'
                                    print(mode)

                                else:

                                    #   print(lmList[4], lmList[8])
                                    x1, y1 = lmList[8][1], lmList[8][2]
                                    x2, y2 = lmList[12][1], lmList[12][2]

                                    cv2.circle(image, (x1, y1), 7, (255, 255, 255), cv2.FILLED)
                                    cv2.circle(image,(x2,y2),15,(255,0,255),cv2.FILLED) #원으로 표시
                                if (lmList[0][1]-lmList[-1][1] >30):
                                    print("<---")
                                    active = 0
                                    mode = 'N'

                                elif(lmList[0][1]-lmList[-1][1] < -30 ):
                                    print("--->")
                                    active = 0
                                    mode = 'N'
                                    self.urlconnect()

                            # if (angle >= 135 or angle < -135):
                            #     print("<---");
                            # elif (angle >= 135 or angle < -135):
                            #     print("--->");



                        ######################################주먹쥐면 커서모드 전환#########################################
                        if (fingers == [0, 0, 0, 0, 0]) & (active == 0): #주먹쥐면 커서모드 전환
                            mode = 'Cursor'
                            active = 1
                        # elif (fingers == [0, 1, 0, 0, 0] ) & (active == 0):
                        #     mode = 'Scroll'
                        #     act###ive = 1
                        if mode == 'Cursor':
                            active = 1
                            cv2.rectangle(image, (30, 20), (620, 470), (255, 255, 255), 3)
                            if fingers == [1, 1, 1, 1, 1]: #손가락 다피면  커서모드에서 나감
                                active = 0
                                mode = 'N'
                                print(mode)
                            else:
                                if len(lmList) != 0:
                                    x1, y1 = lmList[8][1], lmList[8][2]
                                    w, h = autopy.screen.size()
                                    X = int(np.interp(x1, [110, 620], [0, w - 1]))
                                    Y = int(np.interp(y1, [20, 350], [0, h - 1]))
                                    cv2.circle(image, (lmList[8][1], lmList[8][2]), 7, (255, 255, 255), cv2.FILLED)
                                    cv2.circle(image, (lmList[4][1], lmList[4][2]), 10, (0, 255, 0), cv2.FILLED)  # thumb

                                    if X % 2 != 0:
                                        X = X - X % 2
                                    if Y % 2 != 0:
                                        Y = Y - Y % 2
                                    print(X, Y)
                                    autopy.mouse.move(X, Y)
                                    #  pyautogui.moveTo(X,Y)
                                    if fingers[0] == 0:
                                        cv2.circle(image, (lmList[4][1], lmList[4][2]), 10, (0, 0, 255),
                                                   cv2.FILLED)  # thumb
                                        autopy.mouse.click()
######################################### 스크롤모드 전환#########################################
                        # if mode == 'Scroll':
                        #     active = 1
                        #     #   print(mode)
                        #     cv2.rectangle(image, (200, 410), (245, 460), (255, 255, 255), cv2.FILLED)
                        #     if len(lmList) != 0:
                        #         if fingers == [0, 1, 0, 0, 0]:
                        #             # print('up')
                        #             # time.sleep(0.1)
                        #             pyautogui.scroll(300)
                        #
                        #         if fingers == [0, 1, 1, 0, 0]:
                        #             # print('down')
                        #             #  time.sleep(0.1)
                        #             pyautogui.scroll(-300)
                        #         elif fingers == [0, 0, 0, 0, 0]:
                        #             active = 0
                        #             mode = 'N'

#########################################            출력        #########################################

                cv2.imshow('HAND GESTURE', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()
