/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - research_on_logistics_information
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`research_on_logistics_information` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `research_on_logistics_information`;

/*Table structure for table `receiver` */

DROP TABLE IF EXISTS `receiver`;

CREATE TABLE `receiver` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `receiver` */

insert  into `receiver`(`id`,`name`,`email`,`pwd`,`pno`,`addr`) values (1,'Fathima','cse.takeoff@gmail.com','Fathima@506','6302589741','234, Srinihita womens hostel,\r\nbalaji colony,\r\ntirupati, chittoor dist,\r\nAP'),(2,'Keerthana','keerthana123@gmail.com','Keerthana@123','6308989089','Kavali, Prakasam,AP');

/*Table structure for table `request_files` */

DROP TABLE IF EXISTS `request_files`;

CREATE TABLE `request_files` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fid` int(10) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pkey` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'Request',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `request_files` */

insert  into `request_files`(`id`,`fid`,`name`,`fname`,`email`,`pkey`,`status`) values (1,13,'Lakshmi','cloud data','cse.takeoff@gmail.com','7ccdfbbc','Accepted'),(2,14,'Lakshmi','abstact for cyber security','cse.takeoff@gmail.com','5f91243b','Accepted'),(3,15,'Lakshmi','abstact for cyber security','cse.takeoff@gmail.com','7b67fe09','Request'),(4,16,'Rupesh','AES methodology','keerthana123@gmail.com','3b54074b','Accepted');

/*Table structure for table `sender` */

DROP TABLE IF EXISTS `sender`;

CREATE TABLE `sender` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `sender` */

insert  into `sender`(`id`,`name`,`email`,`pwd`,`pno`,`addr`) values (1,'Lakshmi','lakshmi@gmail.com','Lakshmi@123','9630258741','303, AVR Buildings, Balaji Colony  Opp S.V.music College, Tirupati, Chittoor Dist, Andhra Pradesh'),(2,'Rupesh','rupesh452@gmail.com','Rupesh@123','8790989098','Tirupathi');

/*Table structure for table `uploaded_files` */

DROP TABLE IF EXISTS `uploaded_files`;

CREATE TABLE `uploaded_files` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `file` longblob,
  `hash1` varchar(100) DEFAULT NULL,
  `hash2` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time1` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `uploaded_files` */

insert  into `uploaded_files`(`id`,`name`,`email`,`fname`,`file`,`hash1`,`hash2`,`date`,`time1`) values (13,'Lakshmi','lakshmi@gmail.com','cloud data','(Binary/Image)','ab6f471c7b934b895550b6dcfc915d2d4e8ef90f','e2c55e54507156e0e31f70fec6a2231f2e638c41','2021-10-23','13:22:15'),(14,'Lakshmi','lakshmi@gmail.com','abstact for cyber security','>{j>κ�*�:��n��%�H��,��杄eR&!���\0B�ጡ���0\Z��������wȚ��[�IGP�y)��{���qވ|��V]��>�','ab6f471c7b934b895550b6dcfc915d2d4e8ef90f','e2c55e54507156e0e31f70fec6a2231f2e638c41','2021-10-23','18:21:18'),(15,'Lakshmi','lakshmi@gmail.com','abstact for cyber security','>{j>κ�*�:��n��%�H��,��杄eR&!���\0B�ጡ���0\Z��������wȚ��[�IGP�y)��{���qވ|��V]��>���ro��)0��f-Oh\\���ͼN��&ت�!qgQ�@A���j��{��K��@�5��R�Lc��Mp���Do�_<T#�:ΰ��Ӷ���R�','ab6f471c7b934b895550b6dcfc915d2d4e8ef90f','e2c55e54507156e0e31f70fec6a2231f2e638c41','2021-10-23','18:25:42'),(16,'Rupesh','rupesh452@gmail.com','AES methodology','>{j>κ�*�:��n��%�H��,��杄eR&!���\0B�ጡ���0\Z��������wȚ��[�IGP�y)��{���qވ|��V]��>���ro��)0��f-Oh\\���ͼN��&ت�!qgQ�@A���j��{��K��@�5��R�Lc��Mp���Do�_<T#�:ΰ��Ӷ���R�','ab6f471c7b934b895550b6dcfc915d2d4e8ef90f','e2c55e54507156e0e31f70fec6a2231f2e638c41','2021-10-30','18:10:12');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
