# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymysql.cursors
from kaola.items import KaolaGoodItem, KaolaGoodCommentItem, KaolaCategoryItem, KaolaUrlLogItem, KaolaBrandItem, KaolaGoodBrandItem, KaolaGoodCategoryItem


class KaolaPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='kaola',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True
        )
        # 通过cursor 执行sql
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if isinstance(item, KaolaGoodItem):
            # 商品信息入库
            self.insertGood(item)
        elif isinstance(item, KaolaGoodCommentItem):
            # 商品评论入库
            self.insertGoodComment(item)
        elif isinstance(item, KaolaCategoryItem):
            # 商品分类入库
            self.insertCategory(item)
        elif isinstance(item, KaolaUrlLogItem):
            self.insertUrlLog(item)
        elif isinstance(item, KaolaBrandItem):
            self.insertBrand(item)
        elif isinstance(item, KaolaGoodBrandItem):
            self.insertGoodBrand(item)
        elif isinstance(item, KaolaGoodCategoryItem):
            self.insertGoodCategory(item)
        return item

    # 品牌
    def insertBrand(self, item):
        sql = """replace into brand(brandId,brandName) values (%s, %s)"""
        self.cursor.execute(sql, (item['brandId'], item['brandName']))
        self.connect.commit()

    # 商品品牌
    def insertGoodBrand(self, item):
        sql = """replace into good_brand(good_id,brandId) values (%s, %s)"""
        self.cursor.execute(sql, (item['good_id'], item['brandId']))
        self.connect.commit()

    # 品牌
    def insertGoodCategory(self, item):
        sql = """replace into good_category(good_id, categoryId, categoryName, `level`, leaf) values (%s, %s, %s, %s, %s)"""
        self.cursor.execute(sql, (item['good_id'], item['categoryId'], item['categoryName'], item['level'], item['leaf']))
        self.connect.commit()

    # 爬取地址
    def insertUrlLog(self, item):
        sql = """insert into url_log (url, `type`) values (%s, %s)"""
        self.cursor.execute(sql, (item['url'], item['type']))
        self.connect.commit()

    # 商品信息入库
    def insertGood(self, item):
        sql = """replace into goods(good_id,good_name,orig_country,brand,`currentPrice`,`marketPrice`) values (%s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(sql, (item['good_id'], item['name'], item['orig_country'], item['brand'], item['currentPrice'], item['marketPrice']))
        self.connect.commit()

    # 商品信息入库
    def insertGoodComment(self, item):
        sql = """replace into good_comment(good_id, goodsCommentId, appType, orderId, account_id, point, commentContent, createTime, updateTime, zanCount) 
                  values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(sql,
                            (item['good_id'], item['goodsCommentId'], item['appType'], item['orderId'], item['account_id'], item['point'], item['commentContent'], item['createTime'], item['updateTime'], item['zanCount'])
                            )
        self.connect.commit()

    # 商品分类入库
    def insertCategory(self, item):
        sql = """replace into categorys(categoryId, parentId, categoryLevel, categoryName, categoryStatus) values (%s, %s, %s, %s, %s)"""
        self.cursor.execute(sql, (item['categoryId'], item['parentId'], item['categoryLevel'], item['categoryName'], item['categoryStatus']))
        self.connect.commit()