-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: kiosk
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `menu` (
  `menu_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `image` varchar(600) DEFAULT NULL,
  `des` longtext NOT NULL,
  `price` varchar(15) NOT NULL,
  `cat` varchar(30) NOT NULL,
  PRIMARY KEY (`menu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'아메리카노','image/hot_americano_PFFiWUJ.jpg','진하게 로스팅한 커피 원두에서 에스프레소를 추출하여 고유의 원두 풍미를 느낄 수 있는 에스프레소 음료\r\n\r\n\r\n※카페인 함량 : 144.9mg\r\n\r\n카페인 함량은 매장별로 조금씩 다를 수 있습니다.','4100','HOT_COFFEE'),(2,'카페라떼','image/milk_5QMNxlG.jpg','풍부하고 진한 농도의 에스프레소와 \r\n스팀밀크 위에 부드러운 우유 커품을 \r\n살짝 올려준 에스프레소 음료','4600','HOT_COFFEE'),(3,'카페모카','image/moca_EYIx1zl.JPG','진한 초콜릿 모카 시럽과 풍부하고 진한 농도의 에스프레소를 \r\n스팀밀크와 혼합하여 부드러운 휘핑크림을 올린 \r\n달콤한 에스프레소 음료','5100','HOT_COFFEE'),(4,'카푸치노','image/capu_nLoGUU5.png','풍부하고 진한 농도의 에스프레소 위에 \r\n스팀밀크와 부드럽고 풍부한 양의 우유거품을 올린 \r\n에스프레소 음료','4600','HOT_COFFEE'),(5,'카라멜 마끼아또','image/caramel_AV0t7KU.jpg','바닐라 향을 넣은 스팀 밀크 위에 에스프레소 샷을 넣고 \r\n카라멜 소스를 뿌린 달콤한 에스프레소 음료','5600','HOT_COFFEE'),(6,'에스프레소','image/espresso_GHi88Px.JPG','카라멜 향과 더불어 달콤쌉싸름한 맛을 느낄 수 있는 깊고 진한 풍미의 에스프레소 음료\r\n\r\n※카페인 함량: 84.3mg\r\n\r\n카페인 함량은 매장별로 조금씩 다를 수 있습니다.','3300','HOT_COFFEE'),(7,'아이스 아메리카노','image/cold_americano_es9MDeo.jpg','진한게 로스팅한 커피 원두에서 에스프에소를 추출하여 시원한 얼음을 담아 산뜻하게 즐길 수 있는 깔끔한 스타일의 에스프레소 음료\r\n\r\n※카페인 함량:144.9mg\r\n\r\n카페인 함량은 매장별로 조금씩 다를 수 있습니다.','4100','COLD_COFFEE'),(8,'아이스 카페라떼','image/cold_late_S8pKeZ2.jpg','풍부하고 진한 농도의 에스프레소와 \r\n시원한 우유가 어우러진 부드러운 에스프레소 음료','4600','COLD_COFFEE'),(9,'아이스 카페모카','image/ice_m_rr0FzEp.jpg','모카 시럽과 풍부한 에스프레소를 \r\n신선한 우유와 혼합하여 진한 초콜릿 맛이 가득한 \r\n에스프레소 음료','5100','COLD_COFFEE'),(10,'아이스 카푸치노','image/ice_capu_OuaDkv0.jpg','에스프레소 샷과 시원한 우유에 \r\n부드러운 거품이 얹어진 시원한 음료','4600','COLD_COFFEE'),(11,'콜드브루','image/cold_brew_6MOIi2g.JPG','커피 본연의 깊은 풍미와 단맛이 느껴지는 부드럽고 깔끔한 콜드브루 커피\r\n\r\n※카페인 함량 : 196mg\r\n\r\n카페인 함량은 매장별로 조금씩 다를 수 있습니다.','4500','COLD_COFFEE'),(12,'콜드브루 라떼','image/cold_brew_latte_n2DVSbb.JPG','콜드브루와 우유가 어우러져 \r\n더욱 부드럽게 즐길 수 있는 콜드브루 라떼','5000','COLD_COFFEE'),(13,'딸기요거트 스무디','image/berry_8dNxnb8.jpg','남녀노소 누구나 좋아하는 딸기와 \r\n상큼한 요거트가 조화롭게 어우러진 메뉴','5400','BEVERAGE'),(14,'자두 스무디','image/jadu_UYNSSKz.jpg','달콤한 여름향기를 머금은 자두를 \r\n가장 많있고 시원하게 즐길 수 있는 메뉴','5700','BEVERAGE'),(15,'망고 스무디','image/mango_lCRBmrv.jpg','부드러운 황금빛 속살의 골드망고가 \r\n들어간 고급스러운 달콤함의 스무디','5800','BEVERAGE'),(16,'청포도 스무디','image/grape_EfHDzgA.jpg','시원달콤한 청포도 과즙과 \r\n알갱이가 쏙쏙 들어오는 재미가 일품인 음료','5800','BEVERAGE'),(17,'민트 프라페','image/mint_iTOjyG4.jpg','진한 민트향과 초콜렛칩이 가득 들어있는 메뉴로 \r\n여성들에게 큰 인기를 받고 있는 음료','5900','BEVERAGE'),(20,'허니 레몬티','image/honey_lemon_TlxDg3Y.JPG','진한 TWG 프렌치 얼그레이 베이스에 \r\n달콤한 꿀과 상큼한 레몬이 더해진 티','5500','BEVERAGE'),(21,'아이스 허니레몬티','image/honey_lemon_ice_Ity7Ze6.JPG','진한 TWG 프렌치 얼그레이 베이스에 \r\n달콤한 꿀과 상큼한 레몬이 더해진 티','5500','BEVERAGE'),(22,'수박 주스','image/watermelon_VENBVOV.JPG','수박을 통쨰로 갈아 넣어 만든 \r\n시원하고 달콤한 수박 주스','5900','BEVERAGE'),(24,'브라우니','image/brownie_DOEpi26.jpg','카카오 향이 진한 초콜릿의 풍미와 \r\n쫀득한 카스라가 어우러져 중독성 있는 달달한 케잌','4500','BAKE'),(25,'레드벨벳 케이크','image/red_GlFEHIm.jpg','붉은 컬러의 레드벨벳 4단 시트에 \r\n과일 데코레이션으로 상큼함을 더하고, \r\n진한 크림치즈로 아이싱한 케이크','5200','BAKE'),(26,'당근 케이크','image/carrot_gRCiiRX.jpg','담백한 당근과 상큼한 오렌지 필로 \r\n심각을 살린 촉촉한 당근시트와 \r\n크림치즈를 풍성하게 레이어한 영국식 티 케이크','5200','BAKE'),(27,'치즈 케이크','image/cheese_AgqrPcd.jpg','부드럽고 촉촉한 식감과 \r\n진한 치즈 맛을 느낄 수 있는 \r\n뉴욕스타일의 구움 치즈 케잌','4800','BAKE'),(28,'초콜릿 무스','image/cho.jpg','다크, 밀크, 화이트 세 가지 초콜릿을 \r\n한 번에 즐길 수 있는 \r\n트리플 초콜렛 레이어 무스 케잌','5100','BAKE');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-09 22:50:09
