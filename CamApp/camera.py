# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
# from tensorflow.keras.preprocessing.image import img_to_array
# from tensorflow.keras.models import load_model
# from imutils.video import VideoStream
# import imutils
# import cv2, os, urllib.request
# import numpy as np
# from django.conf import settings
# import threading
# bg=None


# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()
#     def segment(image,threshold=25):
#         global bg

#         diff=cv2.absdiff(bg.astype("uint8"),image)
#         thresholded=cv2.threshold(diff,threshold,255,cv2.THRESH_BINARY)
#         cnts,_ = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#오류발생지점
#         if len(cnts)==0:
#             return
#         else:
#             segemented=max(cnts,key=cv2.contourArea)
#             return(thresholded,segemented)

#     def run_avg(self,image, aWeight):
#         global bg

#         if bg is None:
#             bg = image.copy().astype("float")
#             return
#         cv2.accumulateWeighted(image, bg, aWeight)
        
#     def get_frame(self):
#         top,right,bottom,left=10,350,225,590
#         aWeight=0.5
#         num_frames=0
#         success, image = self.video.read()
#         # 손동작 함수 위치
#         frame_flip = cv2.flip(image, 1)#좌우반전
#         clone=frame_flip.copy()
#         (height,width)=frame_flip.shape[:2]
#         roi=frame_flip[top:bottom,right:left]
#         gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
#         gray=cv2.GaussianBlur(gray,(7,7),0)
#         if num_frames < 30:
#             self.run_avg(gray, aWeight)
#         else:
#             hand = self.segment(gray)
#             if hand is not None:
#                 (thresholded, segemented) = hand

#                 cv2.drawContours(clone, [segemented + (right + top)], -1,
#                                  cv2.imshow(thresholded))
#         cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)
#         num_frames += 1


#         ret, jpeg = cv2.imencode('.jpg', clone)
#         return jpeg.tobytes()

#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()

