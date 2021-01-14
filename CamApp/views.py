from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
import cv2
from django.views.decorators import gzip


def WebCam():
    cap = cv2.VideoCapture(0) #내장캠으로 연결 -> 웹캠 연결 후 번호 수정하기
    while True:
        ret, frame = cap.read()
        ret, encodedframe = cv2.imencode(".jpeg", frame)
        encodedframe = encodedframe.tobytes()
        yield b'--frame\r\n' + b'Content-Type:image/jpeg\r\n\r\n' + encodedframe + b'\r\n'


def index(request):
    return render(request, "CamApp/index.html")


@gzip.gzip_page
def feed(request):
    return StreamingHttpResponse(WebCam(), content_type="multipart/x-mixed-replace; boundary=frame")
