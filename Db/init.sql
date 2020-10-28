CREATE TABLE `ProductCompare`.`category` (
  `cat_id` int NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(45) NOT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;
CREATE TABLE `ProductCompare`.`product_description` (
  `pro_id` int NOT NULL,
  `cat_id` int NOT NULL,
  `rew_id` int DEFAULT NULL,
  `price` varchar(150) NOT NULL,
  `description` varchar(10000) NOT NULL,
  `url` varchar(5000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;
CREATE TABLE `ProductCompare`.`products` (
  `pro_id` int NOT NULL AUTO_INCREMENT,
  `pro_name` varchar(1000) NOT NULL,
  `web_name` varchar(100) NOT NULL,
  PRIMARY KEY (`pro_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;
CREATE TABLE `ProductCompare`.`review` (
  `rew_id` int NOT NULL AUTO_INCREMENT,
  `review` varchar(10000) DEFAULT NULL,
  `rating` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`rew_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;