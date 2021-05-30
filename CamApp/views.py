from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
# from .camera import VideoCamera
from mymenu.handnum import CameraNum
import cv2
import threading

def index(request):
    return render(request, "CamApp/index.html")


def gen(camera): #영상화면 출력
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def feed(request):
    return StreamingHttpResponse(gen(CameraNum()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


#
# @gzip.gzip_page
# def video_feed(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:  # This is bad! replace it with proper handling
#         print("에러입니다...")
#         pass
