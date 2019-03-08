# -*- coding: utf-8 -*-
import scrapy


class MydominSpider(scrapy.Spider):
    name = 'mydomin'
    allowed_domains = ['mydomin.com']
    start_urls = ['http://mydomin.com/']

    def parse(self, response):
        pass
