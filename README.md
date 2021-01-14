# motion_detection_kiosk
2021년 캡스톤 디자인

# Install
- pip install opencv-python
- pip install mysqlclient

# DB
##### 테이블 이름은 kiosk
##### 자세한 설정은 settings.py 참고

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
    FOREIGN KEY (order_num) REFERENCES `Order` (order_id),  
	FOREIGN KEY (menu_num) REFERENCES Menu (Menu_id)  
);  

create table `Order`(  
	order_id int auto_increment primary key,  
    time datetime not null,  
    total_price varchar(15) not null  
);  
