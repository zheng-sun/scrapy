# -*- coding: utf-8 -*-
import scrapy
import pymysql
import pymysql.cursors
import suning.items
import redis
from scrapy.spiders import Spider, CrawlSpider
import six
from scrapy.exceptions import DontCloseSpider
from scrapy import signals
from scrapy_redis.utils import bytes_to_str
from scrapy_redis import scheduler
from scrapy_redis.queue import SpiderStack

class ProductListSpider(Spider):
    name = 'ProductList'
    #redis_key = "ListSpider:start_urls"

    redis_encoding = None
    #allowed_domains = ['list.suning.com']
    #start_urls = ['http://list.suning.com/']

    #def __init__(self, *args, **kwargs):

        # domain = kwargs.pop('domain', '')
        # print(domain)
        # self.allowed_domains = filter(None, domain.split(','))
        # print(self.allowed_domains)
        # super(ProductListSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        print('start_requests')
        return self.next_requests()

    def next_requests(self):
        found = 0
        while found < 30:
            redis_conn = redis.Redis(host='127.0.0.1', port='6379')
            redis_llen = redis_conn.llen('ProductListSpider:start_urls')
            print('next_requests redis_llen:', redis_llen)
            if redis_llen > 0:
                data = redis_conn.lpop('ProductListSpider:start_urls')
                yield self.make_request_from_data(data)
                found += 1
            else:
                break

    def setup_redis(self, crawler=None):
        crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)

    def make_request_from_data(self, data):
        print('make_request_from_data')
        print(data)
        url = data.decode('utf-8')
        # url = bytes_to_str(data, self.redis_encoding)
        print(url)
        return self.make_requests_from_url(url)

    def schedule_next_requests(self):
        print('start11111')
        """Schedules a request if available"""
        # TODO: While there is capacity, schedule a batch of redis requests.
        for req in self.next_requests():
            self.crawler.engine.crawl(req, spider=self)

    def spider_idle(self):
        """Schedules a request if available, otherwise waits."""
        # XXX: Handle a sentinel to close the spider.
        print('spider_idle')
        self.schedule_next_requests()
        raise DontCloseSpider

    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        print('from_crawler')
        obj = super(ProductListSpider, self).from_crawler(crawler, *args, **kwargs)
        obj.setup_redis(crawler)
        return obj

    def parse(self, response):
        # 获取下一页地址
        isNextPage = False
        next_page_list = response.xpath('//div[@class="search-page page-fruits clearfix"]/a/@href').extract()
        for next_page in next_page_list:
            if (response.url == response.urljoin(next_page)):
                isNextPage = True
                continue

            if (isNextPage) :
                UrlLogItem = suning.items.SuningUrlLogItem()
                UrlLogItem['url'] = response.urljoin(next_page)
                SpiderStack.push(UrlLogItem['url'])
