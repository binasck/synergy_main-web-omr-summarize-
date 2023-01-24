/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - omr
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`omr` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `omr`;

/*Table structure for table `career` */

DROP TABLE IF EXISTS `career`;

CREATE TABLE `career` (
  `career_id` int(11) NOT NULL AUTO_INCREMENT,
  `career` varchar(250) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  PRIMARY KEY (`career_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `career` */

insert  into `career`(`career_id`,`career`,`description`,`date`,`time`) values 
(1,'kuhgiu','ffuyiyi','2022-10-20','15:59:47'),
(6,'sdvsd','dsvsv','2022-12-31','19:30:18'),
(7,'bas','lml','2023-01-08','22:05:44'),
(8,'lkjl',';j;j','2023-01-10','14:50:46');

/*Table structure for table `chatbox` */

DROP TABLE IF EXISTS `chatbox`;

CREATE TABLE `chatbox` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `chat` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chatbox` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `complaint` varchar(250) DEFAULT NULL,
  `student_lid` int(11) DEFAULT NULL,
  `reply` varchar(250) DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`date`,`complaint`,`student_lid`,`reply`,`status`) values 
(1,'2022-10-13','khihhih',7,'slkdlkdg','done'),
(2,'2022-12-10','asedrftgyhj',7,'fvrvr','done'),
(3,'0000-00-00','',0,'','');

/*Table structure for table `exam` */

DROP TABLE IF EXISTS `exam`;

CREATE TABLE `exam` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `exam` */

insert  into `exam`(`exam_id`,`exam`,`date`) values 
(4,'ugu','2022-11-30'),
(22,'regergegergerg','2023-01-18'),
(23,'gfdsa','2023-01-11');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback_lid` int(11) DEFAULT NULL,
  `feedback` varchar(250) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`feedback_lid`,`feedback`,`date`) values 
(1,7,'rtgf4r','2022-10-14'),
(2,0,'','0000-00-00');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `type` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'','','staff'),
(3,'iiububu','87676676','staff'),
(4,'efewf','wefew','staff'),
(5,'bin123','lkmk','staff'),
(6,'rtgrt','rtgrtg','staff'),
(7,'user','123','student'),
(8,'aysha@n.com','87676676','staff'),
(9,'dyitti','365667','staff'),
(10,'bin@f.c','765432','staff'),
(11,'tgb','bbbb','staff'),
(12,'staff','1234','staff'),
(13,'admin','tgb','admin'),
(14,'gfds','12345','staff'),
(15,'staff','87676676','staff'),
(16,'iiavada','7t76gayb','staff'),
(17,'rt','rtg','staff'),
(18,'tr','tbvv','staff'),
(19,'sd@gmail.com','sdcdcsdcsdc','staff'),
(20,'gf@gmail.com','gf','staff'),
(21,'sdf@gmail.com','sdf','staff'),
(22,'dfv2@gmail.com','dfv','staff'),
(23,'fgb@d.v','6543454545','staff'),
(24,'sd@gmail.com','6555555555','staff'),
(25,'sd@gmail.com','6342344234','staff'),
(26,'sd@gmail.com','8765424534','staff'),
(27,'sd@gmail.com','8765646455','staff'),
(28,'','',''),
(29,'','',NULL);

/*Table structure for table `material` */

DROP TABLE IF EXISTS `material`;

CREATE TABLE `material` (
  `material_id` int(100) NOT NULL AUTO_INCREMENT,
  `name` char(35) DEFAULT NULL,
  `material` char(250) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `staff_id` int(100) DEFAULT NULL,
  PRIMARY KEY (`material_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `material` */

insert  into `material`(`material_id`,`name`,`material`,`date`,`staff_id`) values 
(3,'qw','/static/material/Screenshot (1).png','2022-11-03',NULL);

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_lid` int(11) DEFAULT '0',
  `notification` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`from_lid`,`notification`,`date`) values 
(8,NULL,'sijgoerjpog','2022-12-22'),
(9,NULL,'knnkl','2023-01-01'),
(10,0,'','0000-00-00'),
(11,14,'gfdsa','2023-01-11'),
(12,13,'juewytrcds','2023-01-08');

/*Table structure for table `question` */

DROP TABLE IF EXISTS `question`;

CREATE TABLE `question` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `question` varchar(100) DEFAULT NULL,
  `option_1` varchar(15) DEFAULT NULL,
  `option_2` varchar(15) DEFAULT NULL,
  `option_3` varchar(15) DEFAULT NULL,
  `option_4` varchar(15) DEFAULT NULL,
  `correct_answer` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

/*Data for the table `question` */

insert  into `question`(`question_id`,`exam_id`,`question`,`option_1`,`option_2`,`option_3`,`option_4`,`correct_answer`) values 
(1,2,'jhgj','ghj','ghj','ghj','ghj','ghj'),
(29,18,'ghkgh','ghjgh','ghjghj','ghjghj','',''),
(33,4,'sefsef','d','tyhth','tyh','erg','tyu');

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `mark` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `result` */

insert  into `result`(`result_id`,`exam_id`,`student_id`,`mark`,`date`) values 
(1,1,7,'20','2022-10-20');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_lid` int(11) DEFAULT NULL,
  `name` varchar(25) DEFAULT NULL,
  `gender` varchar(16) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phone` varchar(13) DEFAULT NULL,
  `photo` varchar(250) DEFAULT NULL,
  `qualification` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`staff_lid`,`name`,`gender`,`place`,`post`,`district`,`email`,`phone`,`photo`,`qualification`) values 
(1,14,'Aysha','Female','rkara','hgfd','gfds','sd@gmail.com','gfds','/static/staff/20221026-114728.jpg','bvcxz'),
(6,19,'zxc','Female','sdv','sdc','sdc','sd@gmail.com','sdcdcsdcsdc','/static/staff/20221221-205604.jpg','sdc'),
(10,23,'fgb','Male','fgb','fgb','fgb','fgb@d.v','6543454545','/static/staff/20221222-154827.jpg','fgb'),
(11,24,'rgbrbtgb','Male','rtgrtg','rtgrt','rtgrtg','sd@gmail.com','6555555555','/static/staff/20221222-160846.jpg','4444'),
(13,26,'Binas','Male','fgb','fgbfb','fgbff','sd@gmail.com','8765424534','/static/staff/20221222-162542.jpg','fgbfb'),
(14,27,'wwwerw','Male','etrte','trrt','erte','sd@gmail.com','8765646455','/static/staff/20221222-163322.jpg','fghgh');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_lid` int(11) DEFAULT NULL,
  `name` varchar(25) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phone` varchar(13) DEFAULT NULL,
  `photo` varchar(25) DEFAULT NULL,
  `qualification` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`student_id`,`student_lid`,`name`,`gender`,`place`,`post`,`district`,`email`,`phone`,`photo`,`qualification`) values 
(1,7,'','','','','','','','',''),
(2,0,'','','','','','','','','');

/*Table structure for table `winner` */

DROP TABLE IF EXISTS `winner`;

CREATE TABLE `winner` (
  `winner_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `details` varchar(25) DEFAULT NULL,
  `date_of_passout` date DEFAULT NULL,
  PRIMARY KEY (`winner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `winner` */

insert  into `winner`(`winner_id`,`name`,`photo`,`details`,`date_of_passout`) values 
(1,'JKBBKJ','/static/winner/download.jfif','HGfgGG','2022-12-02'),
(6,'ghgh','/static/winner/ExamRegn_RRAUSCS019_22-12-2022.pdf','gfgn','0000-00-00');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
