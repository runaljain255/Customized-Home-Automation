-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.0.33-community-nt


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema cha1
--

CREATE DATABASE IF NOT EXISTS cha1;
USE cha1;

--
-- Definition of table `areas`
--

DROP TABLE IF EXISTS `areas`;
CREATE TABLE `areas` (
  `areaid` int(10) unsigned NOT NULL auto_increment,
  `areaname` varchar(45) NOT NULL,
  `areadescription` varchar(45) NOT NULL,
  `areapicture` varchar(45) NOT NULL,
  `userid` varchar(45) NOT NULL,
  PRIMARY KEY  (`areaid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `areas`
--

/*!40000 ALTER TABLE `areas` DISABLE KEYS */;
INSERT INTO `areas` (`areaid`,`areaname`,`areadescription`,`areapicture`,`userid`) VALUES 
 (9,'Room','qwertyu','20180916_092732-removebg (3).png','vishaljain2504@gmail.com'),
 (10,'Kitchen','qwerty','7.png','vishaljain2504@gmail.com'),
 (11,'Drawing Room','DR','123.jpg','vishaljain254@gmail.com'),
 (12,'Drawing Room','asdfghj','sacredgames.jpg','ss@s.s');
/*!40000 ALTER TABLE `areas` ENABLE KEYS */;


--
-- Definition of table `switches`
--

DROP TABLE IF EXISTS `switches`;
CREATE TABLE `switches` (
  `switchid` int(10) unsigned NOT NULL auto_increment,
  `userid` varchar(45) NOT NULL,
  `areaid` varchar(45) NOT NULL,
  `purpose` varchar(45) NOT NULL,
  `s_key` varchar(45) NOT NULL,
  `icon` varchar(45) NOT NULL,
  PRIMARY KEY  (`switchid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `switches`
--

/*!40000 ALTER TABLE `switches` DISABLE KEYS */;
INSERT INTO `switches` (`switchid`,`userid`,`areaid`,`purpose`,`s_key`,`icon`) VALUES 
 (11,'vishaljain2504@gmail.com','9','LED','LED_DR','IMG-20190403-WA0010.jpg'),
 (12,'vishaljain254@gmail.com','11','FAN','FAN_DR','123.jpg'),
 (13,'vishaljain254@gmail.com','11','LED','LED','cricket.jpg.jxr'),
 (14,'ss@s.s','12','Fan','FAN_DR','amazonprime.jpg'),
 (15,'ss@s.s','12','Led','LED','amazonprime.jpg');
/*!40000 ALTER TABLE `switches` ENABLE KEYS */;


--
-- Definition of table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `emailid` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `dob` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `picture` varchar(150) NOT NULL,
  PRIMARY KEY  (`emailid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`emailid`,`username`,`mobile`,`dob`,`password`,`picture`) VALUES 
 ('er@m.m','cvbn cxcvbh','1234567','2000-02-02','123','2.png'),
 ('m@m.m','qwertt qwert','1234567','2000-02-02','123','exnode.png'),
 ('ss@s.s','Vishal Jain','9174537339','2000-04-25','123','amazonprime.jpg'),
 ('vishaljain2254@gmail.com','Vishal Jain','9174537339','2000-02-02','123','exnode.png'),
 ('vishaljain2504@gmail.com','Vishal Jain','9174537339','2000-04-25','123','exnode.png'),
 ('vishaljain254000@gmail.com','Vishal Jain','9174537339','2000-02-02','123','asd.jpg'),
 ('vishaljain254@gmail.com','Vishal Jain','9174537339','2000-04-25','123','exnode.png'),
 ('vishaljain25554@gmail.com','Vishal Jain','9174537339','2000-02-02','123','exnode.png'),
 ('vj007@gmail.com','Vishal Jain','9174537339','2000-04-25','123','123.jpg'),
 ('vj008@gmail.com','Vishal Jain','9174537339','2000-02-02','123','asd.jpg');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
