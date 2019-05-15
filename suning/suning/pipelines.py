# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymysql.cursors
from suning.items import SuningUrlLogItem

class SuningPipeline(object):


    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='suning',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True
        )
        # 通过cursor 执行sql
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if isinstance(item, SuningUrlLogItem):
            # 商品信息入库
            self.insertUrlLog(item)
        return item

    # 爬取地址
    def insertUrlLog(self, item):
        sql = """replace into url_log (url, `title`, `type`, RefererUrl) values (%s, %s, %s, %s)"""
        self.cursor.execute(sql, (item['url'], item['title'], item['type'], item['RefererUrl']))
        self.connect.commit()