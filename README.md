# 현재 진행
- 카메라 html에 스트리밍
- 메뉴/주문 디비 연결 
- 회원가입/로그인 
# 해야 할 것
- 주문/결제 페이지 만들기

# motion_detection_kiosk
2021년 캡스톤 디자인

## Install
- pip install opencv-python
- pip install mysqlclient

## DB
##### 테이블 이름: kiosk
*자세한 설정은 settings.py 참고*

테이블 **Order**의 의미로 사용된 부분은 mysql에서 예약어로 사용되기 때문에 **백틱**으로 묶어줘야한다. (백틱은 키보드에서 물결)  
```mysql
use kiosk;

create table Menu(
    menu_id int auto_increment primary key,
    name varchar(30) not null,
    image blob not null,
    des longtext not null,
    price varchar(15) not null,
    cat varchar(30) not null
);

create table Order_List(
    list_id int auto_increment primary key,
    order_num int not null,
    menu_num int not null,
    quatity varchar(3) not null,
    FOREIGN KEY (order_num) REFERENCES Order (order_id),
	FOREIGN KEY (menu_num) REFERENCES Menu (Menu_id)
);

create table Order(  
    order_id int auto_increment primary key,
    time datetime not null,
    total_price varchar(15) not null
);
```
