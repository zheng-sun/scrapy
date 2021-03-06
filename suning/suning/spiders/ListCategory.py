# -*- coding: utf-8 -*-
import scrapy
import pymysql
import pymysql.cursors
import suning.items
from scrapy_redis.spiders import RedisSpider

class ListCategorySpider(RedisSpider):
    name = 'ListCategory'
    redis_key = "ListSpider:start_urls"
    #allowed_domains = ['list.suning.com']
    #start_urls = ['http://list.suning.com/']

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(ListCategorySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
         #获取大分类
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

        #self.updateUrlLogStatus(url=response.url)

