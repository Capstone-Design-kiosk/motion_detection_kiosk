# 사용시
- settings.py에서 본인의 DB로 설정


# Google MediaPipe for Hand Motion

![image10](https://user-images.githubusercontent.com/48480825/135270357-eeb7d2d6-6295-4043-bfe5-4cb84fb44404.gif)
<img src="https://user-images.githubusercontent.com/48480825/135275212-2d0f3ba0-0d36-4e4f-8139-6842585a038d.gif" width="500" height="320">

# 수정 내용
- 메뉴번호를 페이지별 카테고리별 1번 부터 시작하도록 수정
- 포장 여부 선택 checkbox로 변경

cf)
- 손가락인식:mediapipe,autopy 모듈 설치(mymenu/camera.py)
- 커서 인식:
  주먹:커서모드 전환
  보자기:커서모드 아웃
  클릭:검지 손가락으로 커서 이동하고 엄지로누름
- 메인 화면 des글자 수 조절 + 개행 적용되고록 list와 detail수정
- 장바구니 메뉴별 삭제
- 스와이프(2,3 손가락 붙여서 둘 사이 각도 0이면 스와이프 모드로 변환)

# 문제점
- < >페이지 넘김 바 위치 조정 필요
- 선택 쉽게 크기 다 크게
- 

# 현재 완료
- 카메라 html에 스트리밍
- 메뉴/주문 디비 연결
- detail페이지를 주문서 페이지로 설정
- 고객용 페이지 만들기(카테고리별로 분류해서 보이게)
- html css폴더 만들어 참조사용 가능하도록
- 장바구니 페이지 오류 해결 완료
- 카메라 손가락 숫자 인식 (ok, 1~4까지)
- 커서 인식
- 장바구니 메뉴별 삭제
- 스와이프
- 메뉴번호를 페이지별 카테고리별 1번 부터 시작
- 수량과 포장 여부 선택 checkbox
- 첫화면 메인페이지로 변경
- 포장 여부 체크박스 크기 수정

### 관리자 페이지
> - 회원가입/로그인 
> - 메뉴 리스트보기
> - 메뉴 등록하기
> - 메뉴 삭제하기
> - 메뉴 리스트 페이징 
> - 메뉴 상세보기
> - 메뉴 수정하기

##########  해야 할 것  ########## 

### 웹 부분

### 카메라 부분
- 동작 인식 적용되도록 연결
- 스와이프 페이지 연결

# motion_detection_kiosk
2021년 캡스톤 디자인

## Install
- pip install django
- pip install opencv-python
- pip install mysqlclient
- pip install mediapipe
- pip install autopy
- python -m pip install Pillow(이미지 추가 위함)

## DB
##### 테이블 이름: kiosk
*자세한 설정은 settings.py 참고*

```mysql
# 테이블 Order의 의미로 사용된 부분은 예약어라 백틱으로 묶어줌. (백틱은 키보드에서 물결에 있는거)  
use kiosk;

create table Menu(
    menu_id int auto_increment primary key,
    name varchar(30) not null unique,
    image varchar(600),
    des longtext not null,
    price varchar(15) not null,
    cat varchar(30) not null
);

create table `Order`(  
    order_id int auto_increment primary key,
    time datetime not null,
    total_price varchar(15)
);

create table Order_List(
    list_id int auto_increment primary key,
    order_num int not null,
    menu_num int not null,
    quantity INT(100) not null,
    cup VARCHAR(45) default 'here',
    price INT(225),
    menu_name VARCHAR(30),
    FOREIGN KEY (order_num) REFERENCES `Order` (order_id),
	FOREIGN KEY (menu_num) REFERENCES Menu (Menu_id),
	FOREIGN KEY (menu_name) REFERENCES Menu (name)
);
```
