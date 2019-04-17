# -*- coding: utf-8 -*-
import scrapy


class MofcomSpider(scrapy.Spider):
    name = 'mofcom'

    start_urls = ['http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml']

    def parse(self, response):
        print(response)