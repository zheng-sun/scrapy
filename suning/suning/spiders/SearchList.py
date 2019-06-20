# -*- coding: utf-8 -*-
import scrapy
import pymysql
import pymysql.cursors
import suning.items
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
import scrapy_redis.scheduler
from scrapy_redis.queue import SpiderStack

class SearchSpider(RedisSpider):
    name = 'Search'
    redis_key = "SearchSpider:start_urls"

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(SearchSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # 获取下一页地址
        isNextPage = False
        next_page_list = response.xpath('//div[@class="search-page page-fruits clearfix"]/a/@href').extract()
        for next_page in next_page_list:
            if (response.url == response.urljoin(next_page)):
                isNextPage = True
                continue

            if ( isNextPage ):
                UrlLogItem = suning.items.SuningUrlLogItem()
                UrlLogItem['url'] = response.urljoin(next_page)
                print(UrlLogItem['url'])
                yield scrapy.Request(url=UrlLogItem['url'], callback=self.parse, dont_filter=True)
                break

