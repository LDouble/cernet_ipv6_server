-- MySQL dump 10.13  Distrib 5.7.18, for Linux (x86_64)
--
-- Host: localhost    Database: video_server
-- ------------------------------------------------------
-- Server version	5.7.18-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `API`
--

DROP TABLE IF EXISTS `API`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `API` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `api` varchar(255) DEFAULT NULL,
  `method` varchar(24) DEFAULT NULL,
  `desc` varchar(512) DEFAULT NULL,
  `param` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `API`
--

LOCK TABLES `API` WRITE;
/*!40000 ALTER TABLE `API` DISABLE KEYS */;
INSERT INTO `API` VALUES (2,'/api/1.0/token','GET','认证获取token','<p><strong>请求参数:</strong></p>\r\n\r\n<table border=\"1\" cellpadding=\"1\" cellspacing=\"1\" style=\"width:500px\">\r\n	<tbody>\r\n		<tr>\r\n			<td>参数名</td>\r\n			<td>是否可选</td>\r\n		</tr>\r\n		<tr>\r\n			<td>username</td>\r\n			<td>否</td>\r\n		</tr>\r\n		<tr>\r\n			<td>password</td>\r\n			<td>否</td>\r\n		</tr>\r\n	</tbody>\r\n</table>\r\n\r\n<p>备注：在请求头中使用Authorization:base64编码username:password</p>\r\n\r\n<p><strong>返回值</strong></p>\r\n\r\n<table border=\"1\" cellpadding=\"1\" cellspacing=\"1\" style=\"width:500px\">\r\n	<tbody>\r\n		<tr>\r\n			<td>返回类型</td>\r\n			<td>返回值</td>\r\n		</tr>\r\n		<tr>\r\n			<td>json</td>\r\n			<td>\r\n			<p>{<br />\r\n			&nbsp; &nbsp; &quot;error&quot;: &quot;unauthorized&quot;,<br />\r\n			&nbsp; &nbsp; &quot;message&quot;: &quot;未授权&quot;<br />\r\n			} //密码错误时</p>\r\n\r\n			<p>{<br />\r\n			&nbsp; &nbsp; &quot;expiration&quot;: 3600,<br />\r\n			&nbsp; &nbsp; &quot;token&quot;: &quot;eyJleHAiOjE1MTk0NzYzNjcsImlhdCI6MTUxOTQ3Mjc2NywiYWxnIjoiSFMyNTYifQ.eyJpZCI6MX0.</p>\r\n\r\n			<p>DjGPVBWPCZSHx5C4yU6LqDgwz2C4OWnJVo9-ogygRus&quot;<br />\r\n			}&nbsp; //正确情况</p>\r\n			</td>\r\n		</tr>\r\n	</tbody>\r\n</table>\r\n\r\n<p>&nbsp;</p>\r\n');
/*!40000 ALTER TABLE `API` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TV`
--

DROP TABLE IF EXISTS `TV`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TV` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(512) DEFAULT NULL,
  `name` varchar(512) DEFAULT NULL,
  `type` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TV`
--

LOCK TABLES `TV` WRITE;
/*!40000 ALTER TABLE `TV` DISABLE KEYS */;
INSERT INTO `TV` VALUES (1,'http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8','CCTV',4);
/*!40000 ALTER TABLE `TV` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('78db240ccd59');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nav`
--

DROP TABLE IF EXISTS `nav`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nav` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `blue` varchar(255) DEFAULT NULL,
  `method` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nav`
--

LOCK TABLES `nav` WRITE;
/*!40000 ALTER TABLE `nav` DISABLE KEYS */;
INSERT INTO `nav` VALUES (1,'系统设置','admin','system','nav'),(2,'导航添加','admin','nav_add','admin'),(3,'导航列表','admin','nav_lists','admin'),(4,'系统设置','admin','system','admin'),(5,'用户管理','user','user_lists','nav'),(6,'用户列表','user','user_lists','user'),(8,'用户添加','user','user_add','user'),(9,'角色列表','role','role_lists','user'),(10,'角色添加','role','role_add','user'),(11,'电视管理','tv','tv_lists','nav'),(12,'电视台列表','tv','tv_lists','tv'),(13,'电视增加','tv','tv_add','tv'),(14,'节目列表','tv','tv_program','tv'),(15,'播放日志','tv','tv_log','tv'),(16,'推荐日志','tv','recommend_log','tv'),(17,'API管理','api','api_lists','nav'),(18,'API列表','api','api_lists','api'),(19,'API添加','api','api_add','api');
/*!40000 ALTER TABLE `nav` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recommend_log`
--

DROP TABLE IF EXISTS `recommend_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recommend_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(512) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `feedback` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recommend_log`
--

LOCK TABLES `recommend_log` WRITE;
/*!40000 ALTER TABLE `recommend_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `recommend_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(125) DEFAULT NULL,
  `desc` varchar(125) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'普通用户','普通用户用于电视上传日志'),(2,'管理员','管理员用户');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_log`
--

DROP TABLE IF EXISTS `tv_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `program` varchar(255) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `is_recommend` tinyint(1) DEFAULT NULL,
  `time` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_log`
--

LOCK TABLES `tv_log` WRITE;
/*!40000 ALTER TABLE `tv_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `tv_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_program`
--

DROP TABLE IF EXISTS `tv_program`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_program` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `program_name` varchar(255) DEFAULT NULL,
  `tv_name` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `day` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `program_name` (`program_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_program`
--

LOCK TABLES `tv_program` WRITE;
/*!40000 ALTER TABLE `tv_program` DISABLE KEYS */;
/*!40000 ALTER TABLE `tv_program` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `device` varchar(255) DEFAULT NULL,
  `info` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_email` (`email`),
  UNIQUE KEY `ix_user_username` (`username`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin',NULL,2,'pbkdf2:sha256:50000$94k2Mh7p$001180d9fba31f2f97120ded4267cac75e6adb4c15da2e100e9002ec3de64e1e','admin@test.com',NULL,NULL),(2,'13020031085',NULL,2,'pbkdf2:sha256:50000$esqxxqPp$937084e473ae1be993ec352161e2e4a5448f2cfda0ecfd5cfbc6b08440155d54','11',NULL,NULL),(3,'13020031082',NULL,NULL,'pbkdf2:sha256:50000$Mqa8tTMS$413407a161883b767a42cc019851c554d0c9fd002a1eecf27e71fac3b904cc19','1234',NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-01  7:16:27
