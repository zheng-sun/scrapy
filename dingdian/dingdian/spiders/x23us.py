# -*- coding: utf-8 -*-
import scrapy


class X23usSpider(scrapy.Spider):
    name = 'x23us'
    allowed_domains = ['www.x23us.com']
    start_urls = ['http://www.x23us.com/']

    def parse(self, response):
        pass
