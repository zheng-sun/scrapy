# -*- coding: utf-8 -*-
import scrapy


class TmailSpider(scrapy.Spider):
    name = 'tmail'
    allowed_domains = ['list.tmall.com']
    start_urls = ['http://list.tmall.com/']

    def parse(self, response):
        pass
