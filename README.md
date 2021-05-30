# 사용시
- settings.py에서 본인의 DB로 설정

# 수정 내용
- order_list에 menu_name VARCHAR(30) 추가, FK MENU에 name
- menu에 name에 unique 추가 설정
- 장바구니 추가 시 메뉴 이름이 아니라 번호가 출력 해결 
- 장바구니 추가 시 주문번호 가장 최신 번호로 넘어가도록 해결
  (보고서에 제출한 문제점 중 DB에 주문없을 때의 오류도 해결)

# 문제점
-

# 현재 완료
- 카메라 html에 스트리밍
- 메뉴/주문 디비 연결
- detail페이지를 주문서 페이지로 설정
- 고객용 페이지 만들기(카테고리별로 분류해서 보이게)
- html css폴더 만들어 참조사용 가능하도록
- 장바구니 페이지 오류 해결 완료
- 카메라 손가락 숫자 인식 (ok, 1~4까지)
### 관리자 페이지
> - 회원가입/로그인 
> - 메뉴 리스트보기
> - 메뉴 등록하기
> - 메뉴 삭제하기
> - 메뉴 리스트 페이징 
> - 메뉴 상세보기
> - 메뉴 수정하기

# 해야 할 것
### 카메라 부분
손바닥 
- 모션인식 전 손바닥을 인식(camera.py왜 인식안되는지 모르겠음)
- Hand.py,handmotion.py는 무시해도됨(시도해봤던 파일들)
숫자
- 번호 인식해  DB에 넘기기 or 리턴값으로 해서 바로 메뉴 부분과 연결

스와이프(상하, 좌우)
- 카메라 손동작 인식으로 페이지 전환 (상하)
- 카메라 손동작 인식으로 카페고리별 페이지 전환 (좌우)
  
### 메뉴 부분
-(지금 결제부분이 없는데 만들것인지 말것인지)
- UI 꾸미기 키오스크 화면 처럼 (비율 16:9)


# motion_detection_kiosk
2021년 캡스톤 디자인

## Install
- pip install django
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
