# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from selenium import webdriver


class JingdongSpider(Spider):
    name = 'jingdong'

    def __init__(self):
        self.browser = webdriver.Chrome("D:\\360data\\Anaconda3\\Lib\\site-packages\\selenium\\webdriver\\chromedriver.exe")
        self.browser.set_page_load_timeout(30)

    def closed(self,spider):
        print("spider closed")
        self.browser.close()

    def start_requests(self):
        start_urls = ['http://list.suning.com/0-20006-0.html']
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        #selector = response.xpath('//ul[@class="gl-warp clearfix"]/li')
        selector = response.xpath('//ul[@class="general clearfix"]/li')
        print(len(selector))
        print('---------------------------------------------------')

