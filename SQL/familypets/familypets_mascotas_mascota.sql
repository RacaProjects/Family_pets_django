-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: familypets
-- ------------------------------------------------------
-- Server version	9.4.0

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
-- Table structure for table `mascotas_mascota`
--

DROP TABLE IF EXISTS `mascotas_mascota`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mascotas_mascota` (
  `fecha_registro` datetime(6) NOT NULL,
  `nombre_mascota` varchar(50) NOT NULL,
  `raza_mascota` varchar(50) NOT NULL,
  `edad_mascota` int NOT NULL,
  `detalles_adicionales` longtext NOT NULL,
  `foto_mascota` varchar(100) DEFAULT NULL,
  `fundacion` varchar(100) DEFAULT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tamano_mascota` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mascotas_mascota`
--

LOCK TABLES `mascotas_mascota` WRITE;
/*!40000 ALTER TABLE `mascotas_mascota` DISABLE KEYS */;
INSERT INTO `mascotas_mascota` VALUES ('2025-10-11 07:28:47.984324','Azabache 2','Coocker',5,'Temperamento agresivo','fotos_mascotas/Azabache2.jpg','Fundacion patas',3,'Mediano'),('2025-10-11 08:19:59.651696','registro de prueba','NA',10,'Registro de prueba','fotos_mascotas/prueba2.jpg','prueba',4,'pequeño');
/*!40000 ALTER TABLE `mascotas_mascota` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-11  5:41:05
