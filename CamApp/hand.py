import time

import mediapipe as mp
import cv2
import numpy as np
import os
import pyautogui, autopy
import random
import time
from tensorflow.keras.models import load_model
max_num_hands = 1
classes = {
    0:'number',10:'ok',1:'one',2:'two',3:'three',4:'four',5:'cursor',
}
# MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=max_num_hands,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# Gesture recognition model
model = load_model('CamApp/hand2.h5')
active = 0
tipIds = [4, 8, 12, 16, 20]  # 손가락 5개 번호
overlayList = []
# active = 0
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands
# folderPath = "FingerImages"  # 손가락 번호 이미지
# myList = os.listdir(folderPath)
# tipIds = [4, 8, 12, 16, 20]  # 손가락 5개 번호
# overlayList = []
# fingernum=-1
# for imPath in myList:
#     image = cv2.imread(f'{folderPath}/{imPath}')
#     # print(f'{folderPath}/{imPath}')
#     overlayList.append(image)
#
# # Gesture recognition model
# file = np.genfromtxt('CamApp/gesture_train.csv', delimiter=',')
# angle = file[:,:-1].astype(np.float32)
# label = file[:, -1].astype(np.float32)
# knn = cv2.ml.KNearest_create() #최근접 알고리즘을 통해 학습
#
# knn.train(angle, cv2.ml.ROW_SAMPLE, label)

class CAMERA(object):
    def __init__(self):

        cap = cv2.VideoCapture(0)
        # cap = cv2.VideoCapture(1) #웹캠으로 연결시
        active = 0
        joint_list = [[3,2,1,180],[8,7,6,180], [12, 10,9,180], [16, 14, 13,180], [20, 18, 17,180]]#엄지부터 새끼손가락까지(관절1,2,3,각도)
        def draw_finger_angles(image, results, joint_list):  # 손가락 각도

            # Loop through hands
            for hand in results.multi_hand_landmarks:
                # Loop through joint sets
                for joint in joint_list:
                    a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])  # First coord
                    b = np.array([hand.landmark[joint[1]].x, hand.landmark[joint[1]].y])  # Second coord
                    c = np.array([hand.landmark[joint[2]].x, hand.landmark[joint[2]].y])  # Third coord

                    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
                    angle = np.abs(radians * 180.0 / np.pi)

                    if angle > 180.0:
                        angle = 360 - angle
                    k=joint_list.index(joint)
                    joint_list[k][3]=angle
                    # print("joint",joint,k,angle) ############각 관절의 각도 확인용

                    cv2.putText(image, str(round(angle, 2)), tuple(np.multiply(b, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            return image

        with mp_hands.Hands(max_num_hands=max_num_hands,min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:

            while cap.isOpened():
                mode = 'N'
                ret, frame = cap.read()
                # BGR 2 RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 좌우반전
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
                if results.multi_hand_landmarks is not None:
                    xList = []  # x좌표
                    yList = []  # y좌표
                    lmList = []  # id,x,y좌표
                    for res in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(image, res, mp_hands.HAND_CONNECTIONS,
                                                  mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2,
                                                                         circle_radius=4),
                                                  mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2,
                                                                         circle_radius=2),
                                                  )
                        joint = np.zeros((21, 3))
                        for j, lm in enumerate(res.landmark):

                            joint[j] = [lm.x, lm.y, lm.z]
                            h, w, c = image.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            xList.append(cx)
                            yList.append(cy)
                            lmList.append([j, cx, cy]) #####손가락 위치 x,y기억
                            if j == 8:  # 2번쨰 손가락이면
                                cv2.circle(image, (cx, cy), 15, (255, 0, 255), cv2.FILLED)  # 원으로 표시

                        # Compute angles between joints
                        v1 = joint[[0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15, 0, 17, 18, 19],
                             :]  # Parent joint
                        v2 = joint[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                             :]  # Child joint
                        v = v2 - v1  # [20,3]   #각 관전에 대한 각도 계산
                        # Normalize v
                        v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                        # Get angle using arcos of dot product
                        angle = np.arccos(np.einsum('nt,nt->n',
                                                    v[[0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18], :],
                                                    v[[1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19],
                                                    :]))  # [15,]

                        angle = np.degrees(angle)  # Convert radian to degree
                        data = np.array([angle], dtype=np.float32)
                        result = model.predict([data]).squeeze()
                        idx = np.argmax(result)
                        # # Inference gesture
                        # data = np.array([angle], dtype=np.float32)
                        # ret, idxnum, neighbours, dist = knn.findNearest(data, 3)
                        # idx = int(idxnum[0][0])
                        cv2.putText(image, text=classes[idx].upper(), org=(45, 375),
                                                                            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(255, 0, 127),
                                                                            thickness=2)
                        draw_finger_angles(image, results, joint_list)


###################################################커서 모드########################################################################
                    # print("mode active",mode, active,joint_list)
                    if (idx==5 ) and mode == 'N':  # 손바닥 다피면 커서모드 전환
                        print("dddddddddd",mode,active)
                        mode = 'cursor'
                    if mode == 'cursor':
                        active = 1
                        cv2.rectangle(image, (30, 20), (620, 470), (255, 255, 255), 3)
                        if idx==0:  # 주먹:  커서모드에서 나감
                            active = 0
                            mode = 'N'
                        else:
                            if len(lmList) != 0:
                                x1, y1 = lmList[0][1], lmList[0][2]
                                w, h = autopy.screen.size()
                                X = int(np.interp(x1, [110, 620], [0, w - 1]))
                                Y = int(np.interp(y1, [20, 350], [0, h - 1]))
                                cv2.circle(image, (lmList[8][1], lmList[8][2]), 7, (255, 255, 255), cv2.FILLED)

                                if X % 2 != 0:
                                    X = X - X % 2
                                if Y % 2 != 0:
                                    Y = Y - Y % 2
                                print(X, Y)
                                autopy.mouse.move(X, Y)
                                time.sleep(random.uniform(0.0005, 0.0005))
                                if (130 < joint_list[0][3] < 170 or joint_list[1][3] < 175 and joint_list[2][
                                    3] < 175 and joint_list[3][3] < 175 and joint_list[4][
                                        3] < 175) and mode == 'Cursor':
                                    mode = ''
                                    cv2.circle(image, (lmList[8][1], lmList[8][2]), 10, (0, 0, 255),
                                               cv2.FILLED)  # thumb
                                    time.sleep(random.uniform(0.0005, 0.0005))
                                    autopy.mouse.click()

                                    print("커서모드선택")



###################################################숫자 모드########################################################################
                    if mode == 'N':
                        active = 1
                        cv2.rectangle(image, (30, 20), (620, 470), (255, 255, 255), 3)
                        if idx==1 :
                            mode='1'
                            if mode=='1' and (joint_list[0][3] <150  and joint_list[1][3] < 174 and joint_list[2][3] < 50 and joint_list[3][3] < 50 and joint_list[4][3] < 50): ###############숫자 1 구부리면 선택가능
                                print("1클릭됨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",mode)
                                autopy.mouse.move(692, 320)  #x,y값 넣으면됨
                                autopy.mouse.click()
                                mode = 'N'

                        if idx == 2 :
                            mode='2'
                            if mode=='2' and ((150<joint_list[0][3] < 170 and joint_list[1][3] < 176 )and joint_list[2][3]< 50  and joint_list[3][3] < 50 and joint_list[4][3] < 50):###############숫자 2 구부리면 선택가능
                                print("2클릭됨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                autopy.mouse.move(862,366)
                                autopy.mouse.click()
                                mode = 'N'

                        if idx == 3:
                            mode='3'
                            if mode=='3' and ((150<joint_list[0][3] < 170  or joint_list[1][3] < 175 or joint_list[2][3]< 170 )and joint_list[3][3]< 50 and joint_list[4][3] < 50):###############숫자 3 구부리면 선택가능
                                print("3클릭됨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                autopy.mouse.move(686,588)
                                autopy.mouse.click()
                                mode = 'N'

                        if idx == 4:
                            if mode=='4' and (joint_list[0][3] < 150 and joint_list[1][3] < 170 and joint_list[2][3]< 170 and joint_list[3][3]< 170 and joint_list[4][3] < 170) :  ###############숫자 4 구부리면 선택가능
                                print("4클릭됨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                autopy.mouse.move(862, 588)
                                autopy.mouse.click()
                                mode = 'N'

###################################################숫자 모드########################################################################
                    if (idx==10 ):  # okay
                        print("okay")
                        autopy.mouse.move(896,800)
                        autopy.mouse.click()
                #########################################            출력        #########################################

                cv2.imshow('HAND GESTURE', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

# import time
#
# import mediapipe as mp
# import cv2
# import numpy as np
# import os
# import pyautogui, autopy
# import random
# import time
#
# max_num_hands = 1
# gesture = {
#     1:'one', 2:'two', 3:'three', 4:'four', 5:'cursor',
#     6:'six', 7:'rock', 8:'spiderman', 9:'two', 10:'ok',
# }
# rps_gesture = {0:'number',5:'cursor',10:'ok'}
# active = 0
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands
# folderPath = "FingerImages"  # 손가락 번호 이미지
# myList = os.listdir(folderPath)
# tipIds = [4, 8, 12, 16, 20]  # 손가락 5개 번호
# overlayList = []
# fingernum=-1
# for imPath in myList:
#     image = cv2.imread(f'{folderPath}/{imPath}')
#     # print(f'{folderPath}/{imPath}')
#     overlayList.append(image)
#
# # Gesture recognition model
# file = np.genfromtxt('CamApp/gesture_train.csv', delimiter=',')
# angle = file[:,:-1].astype(np.float32)
# label = file[:, -1].astype(np.float32)
# knn = cv2.ml.KNearest_create() #최근접 알고리즘을 통해 학습
#
# knn.train(angle, cv2.ml.ROW_SAMPLE, label)
#
# class CAMERA(object):
#     def __init__(self):
#
#         cap = cv2.VideoCapture(0)
#         # cap = cv2.VideoCapture(1) #웹캠으로 연결시
#         active = 0
#         joint_list = [[3,2,1,180],[8,7,6,180], [12, 10,9,180], [16, 14, 13,180], [20, 18, 17,180]]#엄지부터 새끼손가락까지(관절1,2,3,각도)
#         def draw_finger_angles(image, results, joint_list):  # 손가락 각도
#
#             # Loop through hands
#             for hand in results.multi_hand_landmarks:
#                 # Loop through joint sets
#                 for joint in joint_list:
#                     a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])  # First coord
#                     b = np.array([hand.landmark[joint[1]].x, hand.landmark[joint[1]].y])  # Second coord
#                     c = np.array([hand.landmark[joint[2]].x, hand.landmark[joint[2]].y])  # Third coord
#
#                     radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
#                     angle = np.abs(radians * 180.0 / np.pi)
#
#                     if angle > 180.0:
#                         angle = 360 - angle
#                     k=joint_list.index(joint)
#                     joint_list[k][3]=angle
#                     # print("joint",joint,k,angle) ############각 관절의 각도 확인용
#                     cv2.putText(image, str(round(angle, 2)), tuple(np.multiply(b, [640, 480]).astype(int)),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
#             return image
#
#         with mp_hands.Hands(max_num_hands=max_num_hands,min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:
#
#             while cap.isOpened():
#                 mode = 'N'
#                 ret, frame = cap.read()
#                 # BGR 2 RGB
#                 image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 # 좌우반전
#                 image = cv2.flip(image, 1)
#                 # Set flag
#                 image.flags.writeable = False
#                 # Detections
#                 results = hands.process(image)
#                 # Set flag to true
#                 image.flags.writeable = True
#                 # RGB 2 BGR
#                 image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#
#                 #########################################   손가락개수   #########################################
#                 if results.multi_hand_landmarks is not None:
#                     xList = []  # x좌표
#                     yList = []  # y좌표
#                     lmList = []  # id,x,y좌표
#                     for res in results.multi_hand_landmarks:
#                         mp_drawing.draw_landmarks(image, res, mp_hands.HAND_CONNECTIONS,
#                                                   mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2,
#                                                                          circle_radius=4),
#                                                   mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2,
#                                                                          circle_radius=2),
#                                                   )
#                         joint = np.zeros((21, 3))
#                         for j, lm in enumerate(res.landmark):
#
#                             joint[j] = [lm.x, lm.y, lm.z]
#                             h, w, c = image.shape
#                             cx, cy = int(lm.x * w), int(lm.y * h)
#                             xList.append(cx)
#                             yList.append(cy)
#                             lmList.append([j, cx, cy]) #####손가락 위치 x,y기억
#                             if j == 8:  # 2번쨰 손가락이면
#                                 cv2.circle(image, (cx, cy), 15, (255, 0, 255), cv2.FILLED)  # 원으로 표시
#
#                         # Compute angles between joints
#                         v1 = joint[[0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15, 0, 17, 18, 19],
#                              :]  # Parent joint
#                         v2 = joint[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#                              :]  # Child joint
#                         v = v2 - v1  # [20,3]   #각 관전에 대한 각도 계산
#                         # Normalize v
#                         v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]
#
#                         # Get angle using arcos of dot product
#                         angle = np.arccos(np.einsum('nt,nt->n',
#                                                     v[[0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18], :],
#                                                     v[[1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19],
#                                                     :]))  # [15,]
#
#                         angle = np.degrees(angle)  # Convert radian to degree
#
#                         # Inference gesture
#                         data = np.array([angle], dtype=np.float32)
#                         ret, idxnum, neighbours, dist = knn.findNearest(data, 3)
#                         idx = int(idxnum[0][0])
#                     if len(lmList) != 0:
#                         fingers = []
#                         # 엄지
#                         if lmList[tipIds[0]][1] > lmList[tipIds[0 - 1]][1]:  # 오른손
#                             if lmList[tipIds[0]][1] >= lmList[tipIds[0] - 1][1]:
#                                 fingers.append(1)
#                             else:
#                                 fingers.append(0)
#                         elif lmList[tipIds[0]][1] < lmList[tipIds[0 - 1]][1]:  # 왼손
#                             if lmList[tipIds[0]][1] <= lmList[tipIds[0] - 1][1]:
#                                 fingers.append(1)
#                             else:
#                                 fingers.append(0)
#
#                         # 손가락 네개
#                         for id in range(1, 5):
#                             if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
#                                 fingers.append(1)
#
#                             else:
#                                 fingers.append(0)
#
#                         totalFingers = fingers.count(1)
#                         # print(totalFingers) #숫자 출력
#                         if idx in rps_gesture.keys(): ####주먹이랑 okay때 사용
#                             cv2.putText(image, text=rps_gesture[idx].upper(), org=(45, 375),
#                                         fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(255, 0, 127),
#                                         thickness=2)
#                         else:
#                             cv2.putText(image, str(totalFingers), (45, 375), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=5, color=(255, 0, 127),
#                                         thickness=2)
#                         draw_finger_angles(image, results, joint_list)
#
# ###################################################커서 모드########################################################################
#                     print(mode, active)
#                     if (idx==5 ) and mode == 'N':  # 손바닥 다피면 커서모드 전환
#                         print("dddddddddd",mode,active)
#                         mode = 'Cursor'
#                     if mode == 'Cursor':
#                         active = 1
#                         cv2.rectangle(image, (30, 20), (620, 470), (255, 255, 255), 3)
#                         print(mode)
#                         if idx==0 or totalFingers==0:  # 손가락 다피면  커서모드에서 나감
#                             active = 0
#                             mode = 'N'
#                             print(mode)
#                         else:
#                             if len(lmList) != 0:
#                                 x1, y1 = lmList[0][1], lmList[0][2]
#                                 w, h = autopy.screen.size()
#                                 X = int(np.interp(x1, [110, 620], [0, w - 1]))
#                                 Y = int(np.interp(y1, [20, 350], [0, h - 1]))
#                                 cv2.circle(image, (lmList[8][1], lmList[8][2]), 7, (255, 255, 255), cv2.FILLED)
#
#                                 if X % 2 != 0:
#                                     X = X - X % 2
#                                 if Y % 2 != 0:
#                                     Y = Y - Y % 2
#                                 print(X, Y)
#                                 autopy.mouse.move(X, Y)
#                                 time.sleep(random.uniform(0.0005, 0.0005))
#                                 if (130 < joint_list[0][3] < 170 or joint_list[1][3] < 175 and joint_list[2][
#                                     3] < 175 and joint_list[3][3] < 175 and joint_list[4][
#                                         3] < 175) and mode == 'Cursor':
#                                     mode = ''
#                                     cv2.circle(image, (lmList[8][1], lmList[8][2]), 10, (0, 0, 255),
#                                                cv2.FILLED)  # thumb
#                                     time.sleep(random.uniform(0.0005, 0.0005))
#                                     autopy.mouse.click()
#
#                                     print("커서모드선택")
#
#
#
# ###################################################숫자 모드########################################################################
#                     print(totalFingers,mode)
#                     if mode == 'N':
#                         active = 1
#                         cv2.rectangle(image, (30, 20), (620, 470), (255, 255, 255), 3)
#                         if totalFingers==1 and (joint_list[0][3] <150  and joint_list[1][3] < 174 and joint_list[2][3] < 50 and joint_list[3][3] < 50 and joint_list[4][3] < 50): ###############숫자 1 구부리면 선택가능
#                             print("1클릭됨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",mode)
#                             autopy.mouse.move(692, 320)  #x,y값 넣으면됨
#                             autopy.mouse.click()
#
#                         if totalFingers == 2 and ((150<joint_list[0][3] < 170 and joint_list[1][3] < 176 )and joint_list[2][3]< 50  and joint_list[3][3] < 50 and joint_list[4][3] < 50):###############숫자 2 구부리면 선택가능
#                             print("2클릭됨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#                             autopy.mouse.move(862,366)
#                             autopy.mouse.click()
#
#                         if totalFingers == 3 and ((150<joint_list[0][3] < 170  or joint_list[1][3] < 175 or joint_list[2][3]< 170 )and joint_list[3][3]< 50 and joint_list[4][3] < 50):###############숫자 3 구부리면 선택가능
#                             print("3클릭됨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#                             autopy.mouse.move(686,588)
#                             autopy.mouse.click()
#
#                         if totalFingers == 4 and (joint_list[0][3] < 150 and joint_list[1][3] < 170 and joint_list[2][3]< 170 and joint_list[3][3]< 170 and joint_list[4][3] < 170) :  ###############숫자 4 구부리면 선택가능
#                             print("4클릭됨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#                             autopy.mouse.move(862, 588)
#                             autopy.mouse.click()
#
# ###################################################숫자 모드########################################################################
#                     if (idx==10 ):  # 손바닥 다피면 커서모드 전환
#                         print("okay")
#                         autopy.mouse.move(896,800)
#                         autopy.mouse.click()
#                 #########################################            출력        #########################################
#
#                 cv2.imshow('HAND GESTURE', image)
#
#                 if cv2.waitKey(10) & 0xFF == ord('q'):
#                     break
#
#         cap.release()
#         cv2.destroyAllWindows()
#
#
#
# # import cv2
# # import math
# #
# #
# # class Hand:
# #
# #     def __init__(self, binary, masked, raw, frame):
# #         self.masked = masked
# #         self.binary = binary
# #         self._raw = raw
# #         self.frame = frame
# #         self.contours = []
# #         self.outline = self.draw_outline()
# #         self.fingertips = self.extract_fingertips()
# #
# #     def draw_outline(self, min_area=10000, color=(0, 255, 0), thickness=2):
# #         contours, _ = cv2.findContours(
# #             self.binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# #         palm_area = 0
# #         flag = None
# #         cnt = None
# #         for (i, c) in enumerate(contours):
# #             area = cv2.contourArea(c)
# #             if area > palm_area:
# #                 palm_area = area
# #                 flag = i
# #         if flag is not None and palm_area > min_area:
# #             cnt = contours[flag]
# #             self.contours = cnt
# #             cpy = self.frame.copy()
# #             cv2.drawContours(cpy, [cnt], 0, color, thickness)
# #             return cpy
# #         else:
# #             return self.frame
# #
# #     def extract_fingertips(self, filter_value=50):
# #         cnt = self.contours
# #         if len(cnt) == 0:
# #             return cnt
# #         points = []
# #         hull = cv2.convexHull(cnt, returnPoints=False)
# #         defects = cv2.convexityDefects(cnt, hull)
# #         for i in range(defects.shape[0]):
# #             s, e, f, d = defects[i, 0]
# #             end = tuple(cnt[e][0])
# #             points.append(end)
# #         filtered = self.filter_points(points, filter_value)
# #
# #         filtered.sort(key=lambda point: point[1])
# #         return [pt for idx, pt in zip(range(5), filtered)]
# #
# #     def filter_points(self, points, filter_value):
# #         for i in range(len(points)):
# #             for j in range(i + 1, len(points)):
# #                 if points[i] and points[j] and self.dist(points[i], points[j]) < filter_value:
# #                     points[j] = None
# #         filtered = []
# #         for point in points:
# #             if point is not None:
# #                 filtered.append(point)
# #         return filtered
# #
# #     def get_center_of_mass(self):
# #         if len(self.contours) == 0:
# #             return None
# #         M = cv2.moments(self.contours)
# #         cX = int(M["m10"] / M["m00"])
# #         cY = int(M["m01"] / M["m00"])
# #         return (cX, cY)
# #
# #     def dist(self, a, b):
# #         return math.sqrt((a[0] - b[0])**2 + (b[1] - a[1])**2)