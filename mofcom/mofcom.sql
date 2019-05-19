-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.7.24 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  10.1.0.5464
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 mofcom 的数据库结构
CREATE DATABASE IF NOT EXISTS `mofcom` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `mofcom`;

-- 导出  表 mofcom.category 结构
CREATE TABLE IF NOT EXISTS `category` (
  `category_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='分类表';

-- 数据导出被取消选择。
-- 导出  表 mofcom.market 结构
CREATE TABLE IF NOT EXISTS `market` (
  `market_id` int(11) NOT NULL,
  `region_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`market_id`,`region_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='市场';

-- 数据导出被取消选择。
-- 导出  表 mofcom.product 结构
CREATE TABLE IF NOT EXISTS `product` (
  `product_id` int(11) NOT NULL,
  `categroy_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`product_id`,`categroy_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='产品';

-- 数据导出被取消选择。
-- 导出  表 mofcom.product_price_history 结构
CREATE TABLE IF NOT EXISTS `product_price_history` (
  `date` date DEFAULT NULL,
  `product` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `market` varchar(50) DEFAULT NULL,
  UNIQUE KEY `date_product_market` (`date`,`product`,`market`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='价格历史';

-- 数据导出被取消选择。
-- 导出  表 mofcom.region 结构
CREATE TABLE IF NOT EXISTS `region` (
  `region_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`region_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='地区';

-- 数据导出被取消选择。
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
