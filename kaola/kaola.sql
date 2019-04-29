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

-- 导出  表 kaola.brand 结构
CREATE TABLE IF NOT EXISTS `brand` (
  `brandId` int(11) NOT NULL DEFAULT '0',
  `brandName` varchar(100) NOT NULL DEFAULT '0',
  PRIMARY KEY (`brandId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='品牌';

-- 数据导出被取消选择。
-- 导出  表 kaola.categorys 结构
CREATE TABLE IF NOT EXISTS `categorys` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `categoryId` int(11) NOT NULL DEFAULT '0' COMMENT '分类id',
  `parentId` int(11) NOT NULL DEFAULT '0' COMMENT '上级id',
  `categoryLevel` int(11) NOT NULL DEFAULT '0' COMMENT '分类级别',
  `categoryName` varchar(100) NOT NULL DEFAULT '0' COMMENT '分类名称',
  `categoryStatus` tinyint(4) NOT NULL DEFAULT '0' COMMENT '分类状态',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=729 DEFAULT CHARSET=utf8 COMMENT='商品分类id';

-- 数据导出被取消选择。
-- 导出  表 kaola.goods 结构
CREATE TABLE IF NOT EXISTS `goods` (
  `good_id` int(11) NOT NULL COMMENT '商品id',
  `good_name` varchar(200) NOT NULL COMMENT '商品名称',
  `orig_country` varchar(200) NOT NULL COMMENT '产地',
  `brand` varchar(200) NOT NULL COMMENT '品牌',
  `currentPrice` decimal(10,2) NOT NULL COMMENT '售价',
  `marketPrice` decimal(10,2) NOT NULL COMMENT '参考价',
  PRIMARY KEY (`good_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='考拉商品信息表';

-- 数据导出被取消选择。
-- 导出  表 kaola.good_brand 结构
CREATE TABLE IF NOT EXISTS `good_brand` (
  `good_id` int(11) NOT NULL,
  `brandId` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='商品品牌';

-- 数据导出被取消选择。
-- 导出  表 kaola.good_category 结构
CREATE TABLE IF NOT EXISTS `good_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `good_id` int(11) NOT NULL DEFAULT '0' COMMENT '商品id',
  `categoryId` int(11) NOT NULL DEFAULT '0' COMMENT '分类id',
  `categoryName` varchar(50) NOT NULL DEFAULT '0',
  `level` int(11) NOT NULL DEFAULT '0' COMMENT '分类级别',
  `leaf` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1393 DEFAULT CHARSET=utf8 COMMENT='商品分类';

-- 数据导出被取消选择。
-- 导出  表 kaola.good_comment 结构
CREATE TABLE IF NOT EXISTS `good_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `good_id` int(11) NOT NULL DEFAULT '0' COMMENT '商品id',
  `goodsCommentId` varchar(100) DEFAULT NULL COMMENT '考拉商品评论id',
  `appType` varchar(50) NOT NULL DEFAULT '0' COMMENT '评论设备',
  `orderId` varchar(100) NOT NULL DEFAULT '0' COMMENT '订单id',
  `account_id` varchar(200) NOT NULL DEFAULT '0' COMMENT '用户名',
  `point` varchar(50) NOT NULL DEFAULT '0' COMMENT '评分星级',
  `commentContent` text COMMENT '评论内容',
  `createTime` varchar(50) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `updateTime` varchar(50) NOT NULL DEFAULT '0' COMMENT '修改时间',
  `zanCount` varchar(50) NOT NULL DEFAULT '0' COMMENT '点赞数',
  PRIMARY KEY (`id`),
  UNIQUE KEY `goodsCommentId` (`goodsCommentId`),
  KEY `good_id` (`good_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1550083 DEFAULT CHARSET=utf8 COMMENT='商品评论信息';

-- 数据导出被取消选择。
-- 导出  表 kaola.url_log 结构
CREATE TABLE IF NOT EXISTS `url_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `status` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=32635 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
