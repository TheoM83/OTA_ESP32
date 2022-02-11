-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: esp32_maintainer
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `uid` varchar(100) DEFAULT NULL,
  `authorized` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device`
--

LOCK TABLES `device` WRITE;
/*!40000 ALTER TABLE `device` DISABLE KEYS */;
INSERT INTO `device` VALUES (10,'device-TEST','AC:67:B2:36:71:E4',1),(11,'x1','x1',1),(12,'x2','x2',0);
/*!40000 ALTER TABLE `device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device_activity`
--

DROP TABLE IF EXISTS `device_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device_activity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_device` int DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `version` varchar(25) DEFAULT NULL,
  `activity_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_device` (`id_device`),
  CONSTRAINT `device_activity_ibfk_1` FOREIGN KEY (`id_device`) REFERENCES `device` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device_activity`
--

LOCK TABLES `device_activity` WRITE;
/*!40000 ALTER TABLE `device_activity` DISABLE KEYS */;
INSERT INTO `device_activity` VALUES (38,10,'192.168.1.98','1','2022-02-11'),(39,10,'192.168.1.98','1','2022-02-11'),(40,10,'192.168.1.98','1','2022-02-11'),(41,10,'192.168.1.98','1','2022-02-11'),(42,10,'192.168.1.98','1','2022-02-11'),(43,10,'192.168.1.98','1','2022-02-11');
/*!40000 ALTER TABLE `device_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `update_location`
--

DROP TABLE IF EXISTS `update_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `update_location` (
  `id` int NOT NULL AUTO_INCREMENT,
  `server_ip` varchar(100) DEFAULT NULL,
  `server_location` varchar(255) DEFAULT NULL,
  `device_name` varchar(100) DEFAULT NULL,
  `version` double DEFAULT NULL,
  `automatic` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `update_location`
--

LOCK TABLES `update_location` WRITE;
/*!40000 ALTER TABLE `update_location` DISABLE KEYS */;
INSERT INTO `update_location` VALUES (7,'127.0.0.1','Blink.ino.esp32.bin','device-TEST',2,1);
/*!40000 ALTER TABLE `update_location` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-11 16:47:35
