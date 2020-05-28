/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 8.0.19 : Database - newsystem
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`newsystem` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `newsystem`;

/*Table structure for table `news` */

DROP TABLE IF EXISTS `news`;

CREATE TABLE `news` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `content` varchar(2000) NOT NULL,
  `types` varchar(10) NOT NULL,
  `image` varchar(300) DEFAULT NULL,
  `author` varchar(20) DEFAULT NULL,
  `view_count` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `is_valid` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `news_chk_1` CHECK ((`is_valid` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `news` */

insert  into `news`(`id`,`title`,`content`,`types`,`image`,`author`,`view_count`,`created_at`,`is_valid`) values (9,'学习','项目运行前先执行下sql代码，在命令行中cd到该脚本所在的目录，接着进入mysql命令行，输入\'source create_db.sql;\'','娱乐','https://dss2.bdstatic.com/6Ot1bjeh1BF3odCf/it/u=2596763215,2518846960&fm=85&app=92&f=JPEG?w=121&h=75&s=7DA0A95749B4CAC41E11DA47030040F4','d',1,'2020-05-26 18:45:47',1),(10,'学习','项目运行前先执行下sql代码，在命令行中cd到该脚本所在的目录，接着进入mysql命令行，输入\'source create_db.sql;\'','娱乐','https://dss2.bdstatic.com/6Ot1bjeh1BF3odCf/it/u=2596763215,2518846960&fm=85&app=92&f=JPEG?w=121&h=75&s=7DA0A95749B4CAC41E11DA47030040F4','d',1,'2020-05-26 15:00:13',1),(11,'学习','项目运行前先执行下sql代码，在命令行中cd到该脚本所在的目录，接着进入mysql命令行，输入\'source create_db.sql;\'','推荐','https://dss2.bdstatic.com/6Ot1bjeh1BF3odCf/it/u=2596763215,2518846960&fm=85&app=92&f=JPEG?w=121&h=75&s=7DA0A95749B4CAC41E11DA47030040F4','d',1,'2020-05-26 15:00:15',1),(12,'学习','得到','时政新闻','https://dss2.bdstatic.com/6Ot1bjeh1BF3odCf/it/u=2596763215,2518846960&fm=85&app=92&f=JPEG?w=121&h=75&s=7DA0A95749B4CAC41E11DA47030040F4','d',1,'2020-05-26 15:00:18',1),(14,'如何成为一个资深GitHub探手？','dsdsd','时政新闻','','姑姑',NULL,'2020-05-26 18:46:39',1),(15,'1111','dsds','时政新闻','','哈哈',NULL,'2020-05-26 18:46:47',1),(16,'好好','dsd','推荐','','哈哈',NULL,'2020-05-26 18:46:55',1),(17,'如何成为一个资深GitHub探手？','大声道','时政新闻','','哈哈',0,'2020-05-26 18:40:39',1),(18,'如何成为一个资深GitHub探手？','嘻嘻','推荐','certificate.jpg','嘻嘻',0,'2020-05-26 18:43:00',1),(19,'滚滚滚','gungun','推荐','781C04DC02D434BDB025CBE5293FB5AE.jpg','哈哈',0,'2020-05-26 18:47:11',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
