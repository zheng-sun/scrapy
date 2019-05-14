# -*- coding: utf-8 -*-
import scrapy
import pymysql
import pymysql.cursors
import suning.items

class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ['list.suning.com']
    #start_urls = ['http://list.suning.com/']

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='suning',
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
        sql = """select url from url_log where type = 'category' and status = 0 limit 1"""
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return_data = []
        for d in data:
            d_list = list(d)
            return_data.append(d_list[0])
            self.updateUrlLogStatus(d_list[0])
        return return_data

    def parse(self, response):
        # product_list = response.xpath('//ul[@class="general clearfix"]/li')
        # for product in product_list:
        #     url = product.xpath('div[@class="item-bg"]/div[@class="product-box"]/div[@class="res-info"]/div[@class="title-selling-point"]/a/@href').extract_first()
        #     title = product.xpath('div[@class="item-bg"]/div[@class="product-box"]/div[@class="res-info"]/div[@class="title-selling-point"]/a/text()').extract_first()
        #     UrlLogItem = suning.items.SuningUrlLogItem()
        #     UrlLogItem['url'] = response.urljoin(url)
        #     UrlLogItem['title'] = title
        #     UrlLogItem['type'] = 'product'
        #     yield UrlLogItem

        next_page = response.xpath('//div[@class="search-page page-fruits clearfix"]')
