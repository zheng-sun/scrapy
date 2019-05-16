# -*- coding: utf-8 -*-
import scrapy
import pymysql
import pymysql.cursors
import suning.items

class ListSpider(scrapy.Spider):
    name = 'list'
    allowed_domains = ['list.suning.com']
    #start_urls = ['http://list.suning.com/']

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

    def updateUrlLogStatus(self, url):
        sql = """
            update url_log set `status` = 1 where `url` = %s
        """
        self.cursor.execute(sql, (url))
        self.connect.commit()

    def start_requests(self):
        #while True:
        urls = self.getUrl()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def getUrl(self):
        # 获取category 爬取地址
        sql = """select url from url_log where type = 'list' and status = 0 limit 1"""
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return_data = []
        for d in data:
            d_list = list(d)
            return_data.append(d_list[0])
        return return_data

    def parse(self, response):
        #  获取大分类
        search_main = response.xpath('//div[@class="search-main introduce clearfix"]/div')

        for category in search_main:
            # 一级分类
            # category_id = list.xpath('@id').extract_first()
            # category_name = list.xpath('h2/text()').extract()
            #parentId = 0

            # 二级分类
            box_data = category.xpath('div[@class="title-box clearfix"]')
            for category_2 in box_data:
                UrlLogItem = suning.items.SuningUrlLogItem()
                href = category_2.xpath('div[@class="t-left fl clearfix"]/a/@href').extract_first()
                title = category_2.xpath('div[@class="t-left fl clearfix"]/a/text()').extract_first()
                UrlLogItem['url'] = response.urljoin(href)
                UrlLogItem['title'] = title
                UrlLogItem['type'] = 'category'
                UrlLogItem['RefererUrl'] = response.url
                yield UrlLogItem

                # 三级分类
                for category_3 in category_2.xpath('div[@class="t-right fl clearfix"]'):
                    href_3 = category_3.xpath('a/@href').extract_first()
                    if href_3 is not None:
                        title_3 = category_3.xpath('a/text()').extract_first()
                        UrlLogItem = suning.items.SuningUrlLogItem()
                        UrlLogItem['url'] = response.urljoin(href_3)
                        UrlLogItem['title'] = title_3
                        UrlLogItem['type'] = 'category'
                        UrlLogItem['RefererUrl'] = response.url
                        yield UrlLogItem

        self.updateUrlLogStatus(url=response.url)

