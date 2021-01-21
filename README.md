# 사용시
- settings.py에서 본인의 DB로 설정
# 수정 내용
- image varchar(600)으로 변경
- python -m pip install Pillow(이미지 추가 위함)
# 현재 진행
- 카메라 html에 스트리밍
- 메뉴/주문 디비 연결 
  
> ### 관리자 페이지
>> - 회원가입/로그인 
>> - 메뉴 리스트보기(로그인 이용후 사용 가능)
>> - 메뉴 등록하기
>> - 메뉴 삭제하기
>> - 메뉴 리스트 페이징 
>> - 메뉴 상세보기
>> - 메뉴 수정하기

# 해야 할 것
- 주문서 만들기
- 고객용 페이지 만들기(카테고리별로 분류해서 보이게) 

# motion_detection_kiosk
2021년 캡스톤 디자인

## Install
- pip install opencv-python
- pip install mysqlclient
- python -m pip install Pillow(이미지 추가 위함)

## DB
##### 테이블 이름: kiosk
*자세한 설정은 settings.py 참고*

```mysql
# 테이블 Order의 의미로 사용된 부분은 예약어라 백틱으로 묶어줌. (백틱은 키보드에서 물결에 있는거)  
use kiosk;

create table Menu(
    menu_id int auto_increment primary key,
    name varchar(30) not null,
    image blob not null ->image varchar(600),
    des longtext not null,
    price varchar(15) not null,
    cat varchar(30) not null
);

create table Order_List(
    list_id int auto_increment primary key,
    order_num int not null,
    menu_num int not null,
    quatity varchar(3) not null,
    FOREIGN KEY (order_num) REFERENCES `Order` (order_id),
	FOREIGN KEY (menu_num) REFERENCES Menu (Menu_id)
);

create table `Order`(  
    order_id int auto_increment primary key,
    time datetime not null,
    total_price varchar(15) not null
);
```
