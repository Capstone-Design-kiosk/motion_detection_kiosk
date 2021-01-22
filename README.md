# 사용시
- settings.py에서 본인의 DB로 설정
# 수정 내용
- order_list 에 price INT(225)로 가격 추가
- order_list 에 cup VARCHAR(45) default 'here'로 테이크아웃여부 추가
- order_list 에 quantity INT(100)로 변경
- order 에 total_price INT(255)로 변경
- Menu DB에 cat={"HOT_COFFEE","COLD_COFFEE","BEVERAGE","BAKE"}
# 문제점
- 장바구니 추가 시 메뉴 이름이 아니라 번호가 출력(수정해야함)
- 주문하기를 누르면 ORDER order_id는 1씩 증가함
  But 처음 로그인 시 주문서 번호는 항상 1이라 나중에 겹치기 때문에 로그인 시
  ORDER의 order_id의 최근 값을 가져와 설정하도록 해야함
  (models.py 에 Myordernum)
# 현재 진행
- 카메라 html에 스트리밍
- 메뉴/주문 디비 연결
- detail페이지를 주문서 페이지로 설정
- 메인 list페이지에 장바구니에 담은 메뉴와 수량,가격과 밑에는 총 가격 출력
  (문제점:메뉴 번호가 아니라 메뉴이름이 나오도록 수정해야 함)
- 고객용 페이지 만들기(카테고리별로 분류해서 보이게) 
  
### 관리자 페이지
> - 회원가입/로그인 
> - 메뉴 리스트보기(로그인 이용후 사용 가능)
> - 메뉴 등록하기
> - 메뉴 삭제하기
> - 메뉴 리스트 페이징 
> - 메뉴 상세보기
> - 메뉴 수정하기

# 해야 할 것
- 카메라 손동작 인식으로 페이지 전환
- 카메라 손동작 인식으로 카페고리별 페이지 전환
- 카메라 손가락 숫자 인식으로 번호 인식해 번호 DB에 넘기기
- html css폴더 만들어 참조사용 가능하도록
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
