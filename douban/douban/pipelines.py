# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors


class DoubanPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='douban',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True
        )
        # 通过cursor 执行sql
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        sql = """insert into list(serial_number,title,rating_num,comment,`desc`) values (%s, %s, %s, %s, %s)"""

        self.cursor.execute(sql, (item['serial_number'], item['title'], item['rating_num'], item['comment'], item['desc'],))
        self.connect.commit()

        return item
