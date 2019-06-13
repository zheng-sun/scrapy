# -*- coding: utf-8 -*-
import scrapy
import pymysql
import pymysql.cursors
import suning.items

class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ['list.suning.com']
    #start_urls = ['http://list.suning.com/']

    def start_requests(self):
        while True:
            urls = self.getUrl()
            for url in urls:
                yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        print(response.code)

        # product_list = response.xpath('//ul[@class="general clearfix"]/li')
        # for product in product_list:
        #     url = product.xpath('div[@class="item-bg"]/div[@class="product-box"]/div[@class="res-info"]/div[@class="title-selling-point"]/a/@href').extract_first()
        #     title = product.xpath('div[@class="item-bg"]/div[@class="product-box"]/div[@class="res-info"]/div[@class="title-selling-point"]/a/text()').extract_first()
        #     UrlLogItem = suning.items.SuningUrlLogItem()
        #     UrlLogItem['url'] = response.urljoin(url)
        #     UrlLogItem['title'] = title
        #     UrlLogItem['type'] = 'product'
        #     yield UrlLogItem


        # 获取下一页地址
        isNextPage = False
        next_page_list = response.xpath('//div[@class="search-page page-fruits clearfix"]/a/@href').extract()
        for next_page in next_page_list:
            if (response.url == response.urljoin(next_page)):
                isNextPage = True
                continue

            if (isNextPage) :
                UrlLogItem = suning.items.SuningUrlLogItem()
                UrlLogItem['url'] = response.urljoin(next_page)
                UrlLogItem['title'] = ''
                UrlLogItem['type'] = 'category'
                UrlLogItem['RefererUrl'] = response.url
                yield UrlLogItem

                isNextPage = False
                break