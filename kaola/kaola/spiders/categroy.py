# -*- coding: utf-8 -*-
import scrapy
import pymysql
import pymysql.cursors
import kaola.items

class CategroySpider(scrapy.Spider):
    name = 'categroy'
    allowed_domains = ['www.kaola.com']

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
        sql = """select url from url_log where type = 'category' and status = 0 limit 10"""
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return_data = []
        for d in data:
            d_list = list(d)
            return_data.append(d_list[0])
            self.updateUrlLogStatus(d_list[0])
        return return_data

    def parse(self, response):
        # 获取搜索下商品列表
        hreflist = response.xpath('//div[@class="goodswrap promotion"]/a/@href').extract()
        for href in hreflist:
            UrlLogitem = kaola.items.KaolaUrlLogItem()
            UrlLogitem['url'] = response.urljoin(href)
            UrlLogitem['type'] = 'good'
            yield UrlLogitem
            #yield scrapy.Request(response.urljoin(href), callback=self.parse_good, dont_filter=False)

        # 搜索页下一页抓取
        next_page = response.xpath('//div[@class="splitPages"]/a[@class="nextPage"]/@href').extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)