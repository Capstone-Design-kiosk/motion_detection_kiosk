from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
# from .camera import VideoCamera
from .camera import CAMERA
from .models import Menu
from .models import Order
from .models import OrderList
from django.core.paginator import Paginator
trynum=0#프로그램 실행시 처음 사용자인지 여부 확인용
try:
    latestnum = OrderList.objects.latest('order_num')#가장 최신 주문번호
    latestnum2=hash(latestnum.order_num)+1
except OrderList.DoesNotExist:#맨처음 프로그램 실행시 order내용이 아예 없을 때
    latestnum2=1
newnum = latestnum2 + 1  # 결제하기 누르고 다음 사람을 위해 이어지는 주문번호

def index(request):
    return render(request, "CamApp/index.html")


def gen(camera): #영상화면 출력
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    page = request.GET.get('page', 1)
    paginator = Paginator(Menus, 4)  # 9로 변경해야함, 일단 확인차
    menu_list = paginator.get_page(page)




def feed(request):
    return StreamingHttpResponse(gen(CAMERA()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
    # # return StreamingHttpResponse(gen(CameraNum()),
    #                              content_type='multipart/x-mixed-replace; boundary=frame')

# @gzip.gzip_page
# def video_feed(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:  # This is bad! replace it with proper handling
#         print("에러입니다...")
#         pass
