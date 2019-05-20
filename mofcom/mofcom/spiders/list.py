# -*- coding: utf-8 -*-
import scrapy


class ListSpider(scrapy.Spider):
    name = 'price_list'
    allowed_domains = ['nc.mofcom.gov.cn']
    start_urls = ['http://nc.mofcom.gov.cn/']

    def parse(self, response):
        pass
