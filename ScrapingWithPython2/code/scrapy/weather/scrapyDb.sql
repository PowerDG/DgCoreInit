-- create database ScrapyDB Character set 
-- CREATE SCHEMA `scrapydb` DEFAULT CHARACTER SET utf8 ;

CREATE SCHEMA `scrapydb`   CHARACTER SET "utf8" COLLATE 'utf8_general_Ci'
CREATE TABLE `scrapydb`.`weather` (
  `id` INT NULL AUTO_INCREMENT,
  `cityDate` VARCHAR(45) NULL,
  `week` VARCHAR(45) NULL,
  `img` CHAR(20) NULL,
  `temperature` CHAR(12) NULL,
  `weather` CHAR(20) NULL,
  `wind` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE `weather` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cityDate` VARCHAR(45) NULL,
  `week` VARCHAR(45) NULL,
  `img` CHAR(20) NULL,
  `temperature` CHAR(12) NULL,
  `weather` CHAR(20) NULL,
  `wind` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE DATABASE `databasename` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;


INSERT into mysql.user(Host,User,Password)values("%","crawlUSER",password("crwal123"));
-- https://blog.csdn.net/qq_42440234/article/details/83051972
CREATE USER crawlUSER IDENTIFIED BY 'crwal123';

grant all privileges on weather.* to 'crawlUSER'@'%';

FLUSH PRIVILEGES;


-- Python3 MySQL 数据库连接 - PyMySQL 驱动
-- http://www.runoob.com/python3/python3-mysql.html

-- MySQL8初始化、账户创建及权限分配
-- https://blog.csdn.net/sforiz/article/details/81948215

-- MySQL-8.0.11添加新用户设置
-- https://blog.csdn.net/lxx_helloworld/article/details/83376423

-- PyMySQL的基本使用
-- https://www.cnblogs.com/xfxing/p/9322199.html

-- mysql 8.0.12 创建新的数据库、用户并授权
-- https://www.cnblogs.com/xzlive/p/9546964.html