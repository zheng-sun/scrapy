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
        self.browser = webdriver.Chrome("E:\\PythonCode\\scrapy\\chromedriver_73.exe")
        self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        print("spider closed")
        self.browser.close()

    # 截取请求地址获取参数
    def getParam(self, url, file):
        url_split = url.split('?')
        para = {}
        if len(url_split) > 1:
            params = url_split[1].split('&')
            for param in params:
                p = param.split('=')
                para[p[0]] = p[1]

        if para[file] is not None:
            return para[file]
        return ''

    # start_urls = ['http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=13079&craft_index=13233&par_p_index=35']
    # self.crawler.engine.close_spider(self, '计数超过10，停止爬虫!')
    def start_requests(self):
        #self.logger.info("start_requests %s", self.name)
        #start_urls = GetData().getReptile('0', 'price_list')
        start_urls = ['http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=13079&craft_index=13245&par_p_index=34&startTime=2014-01-01&endTime=2014-04-01']
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        region_id = self.getParam(response.url, 'par_p_index')
        
        table = response.xpath('//table[@class="table-01 mt30"]/tr')
        for tr in table:
            tds = tr.xpath('td')
            date = tds[0].xpath('text()').extract_first()
            product = tds[1].xpath('span/text()').extract_first()
            price = tds[2].xpath('span/text()').extract_first()
            unit = tds[2].xpath('text()').extract_first()
            market = tds[3].xpath('a/text()').extract_first()


