# -*- coding: utf-8 -*-
import scrapy
import pymysql
import pymysql.cursors
import kaola.items
import json

class GoodCommentSpider(scrapy.Spider):
    name = 'good_comment'
    allowed_domains = ['search.kaola.com', 'goods.kaola.com']

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='kaola',
            user='root',
            passwd='',
            charset='utf8',
            use_unicode=True
        )
        # 通过cursor 执行sql
        self.cursor = self.connect.cursor()

    def updateUrlLogStatus(self, url):
        sql = """
            update url_log set `status` = 1 where `url` = %s
        """
        self.cursor.execute(sql, (url))
        self.connect.commit()

    def start_requests(self):
        while True:
            urls = self.getUrl()
            for url in urls:
                yield scrapy.Request(url, callback=self.parse)

    def getUrl(self):
        # 获取category 爬取地址
        sql = """select url from url_log where type = 'good_comment' and status = 0 limit 10"""
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return_data = []
        for d in data:
            d_list = list(d)
            return_data.append(d_list[0])
            self.updateUrlLogStatus(d_list[0])
        return return_data

    def parse(self, response):
        dict_json = json.loads(response.body)
        commentPage = dict_json['data']['commentPage']
        if commentPage['totalCount'] > 0:
            good_comment_item = kaola.items.KaolaGoodCommentItem()
            for result in commentPage['result']:
                good_comment_item['good_id'] = result['goodsId']
                good_comment_item['goodsCommentId'] = result['goodsCommentId']
                good_comment_item['appType'] = result['appType']
                good_comment_item['orderId'] = result['orderId']
                good_comment_item['account_id'] = result['accountId']
                good_comment_item['point'] = result['commentPoint']
                good_comment_item['commentContent'] = result['commentContent']
                good_comment_item['createTime'] = result['createTime']
                good_comment_item['updateTime'] = result['updateTime']
                good_comment_item['zanCount'] = result['zanCount']
                yield good_comment_item

            # 获取商品评论下一页数据
            if commentPage['pageNo'] < commentPage['totalPage']:
                good_id = dict_json['data']['commentStat']['goodsId']
                pageNo = commentPage['pageNo'] + 1

                pageNo = str(pageNo)
                good_id = str(good_id)

                apiUrl = 'https://goods.kaola.com/commentAjax/comment_list_new.json?goodsId=' + good_id + '&pageSize=100&pageNo=' + pageNo
                yield scrapy.Request(apiUrl, callback=self.parse)
