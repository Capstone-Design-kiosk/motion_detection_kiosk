import mediapipe as mp
import cv2
import numpy as np
import autopy
import random
import time
import os
from tensorflow.keras.models import load_model
max_num_hands = 1
classes = {
    0:'number',6:'ok',1:'one',2:'two',3:'three',4:'four',5:'cursor',
}
# MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
hands = mp_hands.Hands(
    max_num_hands=max_num_hands,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# Gesture recognition model
model = load_model('CamApp/hand.h5')
active = 0
tipIds = [4, 8, 12, 16, 20]  # 손가락 5개 번호
overlayList = []
heightDifferenceFactor = 0.07
box1=[]
box2=[]
box3=[]
box4=[]
box5=[]
mode='N'
# Gesture recognition model
# file = np.genfromtxt('CamApp/gesture_train.csv', delimiter=',')
# angle = file[:,:-1].astype(np.float32)
# label = file[:, -1].astype(np.float32)
# knn = cv2.ml.KNearest_create() #최근접 알고리즘을 통해 학습
#
# knn.train(angle, cv2.ml.ROW_SAMPLE, label)

class CAMERA(object):
    def __init__(self):
        cap = cv2.VideoCapture(0)
        active = 0
        joint_list = [[8, 5, 12, 9]]  # 2,3손가락
        # joint_list = [[3, 2, 1],[8, 7, 6], [12, 11, 10], [16, 15, 14], [20, 19, 18]]
        # joint_list = [[3, 2, 1, 180], [8, 7, 6, 180], [12, 10, 9, 180], [16, 14, 13, 180],
        #               [20, 18, 17, 180]]  # 엄지부터 새끼손가락까지(관절1,2,3,각도)

        def draw_finger_angles(image, results, joint_list):  # 손가락 각도

            # Loop through hands
            for hand in results.multi_hand_landmarks:
                # Loop through joint sets
                for joint in joint_list:
                    a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])  # 8 x,y좌표
                    b = np.array([hand.landmark[joint[1]].x, hand.landmark[joint[1]].y])  # 5 x,y좌표
                    c = np.array([hand.landmark[joint[2]].x, hand.landmark[joint[2]].y])  # 12 x,y좌표
                    d = np.array([hand.landmark[joint[3]].x, hand.landmark[joint[3]].y])  # 9 x,y좌표

                    radians = np.arctan2(d[1] - c[1], d[0] - c[0]) - np.arctan2(b[1] - a[1], b[0] - a[0])
                    global angles
                    angles = np.abs(radians * 180.0 / np.pi)  # 2,3번째 손가락 각도

                    if angles > 180.0:
                        angles = 360 - angles

                    cv2.putText(image, str(round(angles, 2)), tuple(np.multiply(b, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)  # 각도 표시
            return image

        with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
            while cap.isOpened():
                mode = 'N'
                ret, frame = cap.read()

                # BGR 2 RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Flip on horizontal
                image = cv2.flip(image, 1)

                # Set flag
                image.flags.writeable = False

                # Detections
                results = hands.process(image)

                # Set flag to true
                image.flags.writeable = True

                # RGB 2 BGR
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Rendering results
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
                            lmList.append([j, cx, cy])  #####손가락 위치 x,y기억
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

                        xmin, xmax = min(xList), max(xList)
                        ymin, ymax = min(yList), max(yList)
                        boxW, boxH = xmax - xmin, ymax - ymin
                        box = xmin, ymin, boxW, boxH
                        cv2.rectangle(image, (box[0] - 20, box[1] - 20),
                                      (box[0] + box[2] + 20, box[1] + box[3] + 20), (0, 255, 0), 2)
                        cv2.putText(image, text=classes[idx].upper(), org=(45, 375),
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(255, 0, 127),
                                    thickness=2)

                        draw_finger_angles(image, results, joint_list)



#             ###################################################커서 모드########################################################################
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
                                x1, y1 = lmList[9][1], lmList[9][2]
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
                                # box5.append(box[3])
                                # print("box5", box5)
                                # heightDifferenceThreshold = box5[-1] * heightDifferenceFactor
                                # # if len(box5) > 2 and (
                                #         box5[-1] > box5[-2] + heightDifferenceThreshold)and mode == 'Cursor':  ####100이상 차이나면 클릭 처리
                                #     print("5Zoom in---------------------------")
                                #     box5.clear()
                                if angles<2 and mode=='cursor':
                                    mode = ''
                                    cv2.circle(image, (lmList[8][1], lmList[8][2]), 10, (0, 0, 255),
                                               cv2.FILLED)  # thumb
                                    time.sleep(random.uniform(0.0005, 0.0005))
                                    autopy.mouse.click()

                                    print("커서모드선택")
                    # if (idx==5 ) and box:  # 손바닥 다피면 커서모드 전환
                    #     cv2.rectangle(image, (30, 20), (620, 470), (255, 255, 255), 3)
                    #     if len(lmList) != 0:
                    #         x1, y1 = lmList[8][1], lmList[8][2]
                    #         w, h = autopy.screen.size()
                    #         X = int(np.interp(x1, [110, 620], [0, w - 1]))
                    #         Y = int(np.interp(y1, [20, 350], [0, h - 1]))
                    #         cv2.circle(image, (lmList[8][1], lmList[8][2]), 7, (255, 255, 255), cv2.FILLED)
                    #
                    #         if X % 2 != 0:
                    #             X = X - X % 2
                    #         if Y % 2 != 0:
                    #             Y = Y - Y % 2
                    #         print(X, Y)
                    #         autopy.mouse.move(X, Y)
                    #         time.sleep(random.uniform(0.0005, 0.0005))
                    #         box5.append(box[3])
                    #         print("box5",box5)
                    #         heightDifferenceThreshold = box5[-1] * heightDifferenceFactor
                    #         if len(box5)>2 and (box5[-1] > box5[-2] + heightDifferenceThreshold): ####100이상 차이나면 클릭 처리
                    #             print("5Zoom in---------------------------")
                    #             box5.clear()
                    #             cv2.circle(image, (lmList[8][1], lmList[8][2]), 10, (0, 0, 255),
                    #                        cv2.FILLED)  # thumb
                    #             time.sleep(random.uniform(0.0005, 0.0005))
                    #             autopy.mouse.click()
                    #
                    #             print("커서모드선택")

# ###################################################숫자 모드########################################################################
                    if mode == 'N':
                        active = 1
                        if box and idx==1:
                                box2.clear()
                                box3.clear()
                                box4.clear()
                                box5.clear()
                                box1.append(box[3])
                                print("box1999999999",box1)
                                heightDifferenceThreshold = box1[-1] * heightDifferenceFactor
                                if len(box1)>2 and (box1[-1] > box1[-2] + heightDifferenceThreshold): ####100이상 차이나면 클릭 처리
                                    print("1Zoom in---------------------------")
                                    box1.clear()
                                    autopy.mouse.move(692, 320)  # x,y값 넣으면됨
                                    autopy.mouse.click()
                        elif box and idx==2:
                                box1.clear()
                                box3.clear()
                                box4.clear()
                                box5.clear()
                                box2.append(box[3])
                                print("box2",box2)
                                heightDifferenceThreshold = box2[-1] * heightDifferenceFactor
                                if len(box2)>2 and (box2[-1] > box2[-2] + heightDifferenceThreshold): ####100이상 차이나면 클릭 처리
                                    print("2Zoom in---------------------------")
                                    box2.clear()
                                    autopy.mouse.move(862, 366)
                                    autopy.mouse.click()
                        elif box and idx==3:
                                box1.clear()
                                box2.clear()
                                box4.clear()
                                box5.clear()
                                box3.append(box[3])
                                print("box3",box3)
                                heightDifferenceThreshold = box3[-1] * heightDifferenceFactor
                                if len(box3)>2 and (box3[-1] > box3[-2] + heightDifferenceThreshold): ####100이상 차이나면 클릭 처리
                                    print("3Zoom in---------------------------")
                                    box3.clear()
                                    autopy.mouse.move(686, 588)
                                    autopy.mouse.click()
                        elif box and idx==4:
                                box1.clear()
                                box2.clear()
                                box3.clear()
                                box5.clear()
                                box4.append(box[3])
                                print("box4",box4)
                                heightDifferenceThreshold = box4[-1] * heightDifferenceFactor
                                if len(box4)>2 and (box4[-1] > box4[-2] + heightDifferenceThreshold): ####100이상 차이나면 클릭 처리
                                    print("4Zoom in---------------------------")
                                    box4.clear()
                                    autopy.mouse.move(862, 588)
                                    autopy.mouse.click()
                    # elif box and idx==5:
                    #         box5.append(box[3])
                    #         print("box5",box5)
                    #         heightDifferenceThreshold = box5[-1] * heightDifferenceFactor
                    #         if len(box5)>2 and (box5[-1] > box5[-2] + heightDifferenceThreshold): ####100이상 차이나면 클릭 처리
                    #             print("5Zoom in---------------------------")
                    #             box5.clear()
                    #             autopy.mouse.move(692, 320)  # x,y값 넣으면됨
                    #             autopy.mouse.click()

###################################################숫자 모드########################################################################
                    if (idx==6 ):  # okay
                        box2.clear()
                        box3.clear()
                        box4.clear()
                        box1.clear()
                        print("okay")
                        box5.append(box[3])
                        print("box5", box5)
                        heightDifferenceThreshold = box5[-1] * heightDifferenceFactor
                        if len(box5) > 2 and (box5[-1] > box5[-2] + heightDifferenceThreshold):  ####100이상 차이나면 클릭 처리
                            print("okayZoom in---------------------------")
                            box5.clear()
                            autopy.mouse.move(896, 800)
                            autopy.mouse.click()

                #########################################            출력        #########################################

                cv2.imshow('HAND GESTURE', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()