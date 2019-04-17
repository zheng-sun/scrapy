# -*- coding: utf-8 -*-
import scrapy


class CategroySpider(scrapy.Spider):
    name = 'categroy'
    allowed_domains = ['www.kaola.com']
    start_urls = ['https://www.kaola.com/']

    def parse(self, response):
        categreys = response.xpath('//div[@class="ctgnamebox"]/a/@href').extract()
        print(categreys)
        # for categreys in categreys:
        #
        # pass
