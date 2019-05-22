# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from selenium import webdriver
import mofcom.items
from mofcom.Models.GetData import GetData

class ListSpider(Spider):
    name = 'price_list'


    def __init__(self):
        pass
        # self.browser = webdriver.Chrome("E:\\PythonCode\\scrapy\\chromedriver_73.exe")
        # self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        pass
        print("spider closed")
        self.browser.close()

    def start_requests(self):
        pass
        #pass
        # start_urls = ['http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=13079&craft_index=13233&par_p_index=35']
        # for url in start_urls:
        #     yield Request(url=url, callback=self.parse)

    def parse(self, response):

        pass
