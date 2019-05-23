# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from selenium import webdriver
import mofcom.items
from mofcom.Models.GetData import GetData
#import logging

#logger = logging.getLogger(__name__)

class ListSpider(Spider):
    name = 'price_list'

    def __init__(self):
        pass
        # self.browser = webdriver.Chrome("D:\\PythonCode\\scrapy\\chromedriver_74.exe")
        # self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        pass
        # print("spider closed")
        # self.browser.close()

    # start_urls = ['http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=13079&craft_index=13233&par_p_index=35']
    # self.crawler.engine.close_spider(self, '计数超过10，停止爬虫!')
    def start_requests(self):
        self.logger.info("start_requests %s", self.name)
        start_urls = GetData().getReptile('0', 'price_list')

        for url in start_urls:
            self.log(url['url'])
            yield Request(url=url['url'], callback=self.parse)

    def parse(self, response):

        pass
