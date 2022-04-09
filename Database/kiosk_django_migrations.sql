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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (2,'CamApp','0002_auto_20210115_0104','2021-01-15 02:02:16.227399'),(3,'CamApp','0003_auto_20210115_0322','2021-01-15 02:02:16.235830'),(4,'contenttypes','0001_initial','2021-01-15 02:02:16.342472'),(5,'auth','0001_initial','2021-01-15 02:02:16.656438'),(6,'admin','0001_initial','2021-01-15 02:02:17.777896'),(7,'admin','0002_logentry_remove_auto_add','2021-01-15 02:02:18.131047'),(8,'admin','0003_logentry_add_action_flag_choices','2021-01-15 02:02:18.149401'),(9,'contenttypes','0002_remove_content_type_name','2021-01-15 02:02:18.372104'),(10,'auth','0002_alter_permission_name_max_length','2021-01-15 02:02:18.484696'),(11,'auth','0003_alter_user_email_max_length','2021-01-15 02:02:18.536279'),(12,'auth','0004_alter_user_username_opts','2021-01-15 02:02:18.554154'),(13,'auth','0005_alter_user_last_login_null','2021-01-15 02:02:18.667720'),(14,'auth','0006_require_contenttypes_0002','2021-01-15 02:02:18.675656'),(15,'auth','0007_alter_validators_add_error_messages','2021-01-15 02:02:18.692025'),(16,'auth','0008_alter_user_username_max_length','2021-01-15 02:02:18.819496'),(17,'auth','0009_alter_user_last_name_max_length','2021-01-15 02:02:19.027816'),(18,'auth','0010_alter_group_name_max_length','2021-01-15 02:02:19.068984'),(19,'auth','0011_update_proxy_permissions','2021-01-15 02:02:19.087336'),(20,'sessions','0001_initial','2021-01-15 02:02:19.139913'),(21,'auth','0012_alter_user_first_name_max_length','2021-01-15 10:34:53.312601'),(22,'kiosk','0001_initial','2021-01-15 11:03:13.316900'),(24,'CamApp','0001_initial','2021-09-29 12:09:48.055654'),(25,'mymenu','0001_initial','2021-09-29 12:10:09.550143');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
