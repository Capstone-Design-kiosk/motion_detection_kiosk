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
-- Table structure for table `order_list`
--

DROP TABLE IF EXISTS `order_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `order_list` (
  `list_id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_num` varchar(45) NOT NULL,
  `order_num` int(11) NOT NULL,
  `quantity` int(100) NOT NULL DEFAULT '0',
  `price` int(225) NOT NULL DEFAULT '0',
  `cup` varchar(45) NOT NULL DEFAULT 'here',
  `menu_name` varchar(30) NOT NULL,
  PRIMARY KEY (`list_id`),
  KEY `oder_list_ibfk_2_idx` (`menu_num`) /*!80000 INVISIBLE */
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_list`
--

LOCK TABLES `order_list` WRITE;
/*!40000 ALTER TABLE `order_list` DISABLE KEYS */;
INSERT INTO `order_list` VALUES (52,'4',1,1,4600,'1','카푸치노'),(53,'1',2,1,4100,'1','아메리카노'),(54,'3',3,2,10200,'1','카페모카'),(55,'4',3,2,9200,'1','카푸치노'),(56,'4',4,2,9200,'1','카푸치노'),(57,'3',5,1,5100,'1','카페모카'),(58,'2',6,1,4600,'1','카페라떼'),(60,'2',7,1,4600,'1','카페라떼'),(61,'1',8,1,4100,'0','아메리카노'),(62,'3',9,1,5100,'0','카페모카'),(63,'4',10,2,9200,'1','카푸치노'),(64,'3',11,1,5100,'1','카페모카'),(65,'1',12,2,8200,'1','아메리카노');
/*!40000 ALTER TABLE `order_list` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-09 22:50:08
