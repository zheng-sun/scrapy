# -*- coding: utf-8 -*-
import scrapy
import suning.items

class ListSpider(scrapy.Spider):
    name = 'list'
    allowed_domains = ['list.suning.com']
    start_urls = ['http://list.suning.com/']

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
                href = category_2.xpath('div[@class="t-left fl clearfix"]/a/@href').extract_first()
                type = 'list'
                #parentId = category_id
                #category_id = list.xpath('@id').extract_first()
                #category_name = list.xpath('h2/text()').extract_first()

                # 三级分类
                for category_3 in category_2.xpath('div[@class="t-right fl clearfix"]'):
                    href = category_3.xpath('a/@href').extract_first()
                    type = 'list'


        # allsortLeftLi = response.xpath('//div[@class="allsortLeft"]/ul/li')
        # for left in allsortLeftLi:
        #     UrlLogItem = scrapy.items.SuningUrlLogItem()
        #     UrlLogItem['url'] =

