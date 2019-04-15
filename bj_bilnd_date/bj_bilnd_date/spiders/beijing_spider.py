# -*- coding: utf-8 -*-
import scrapy


class BeijingSpiderSpider(scrapy.Spider):
    name = 'beijing_spider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
