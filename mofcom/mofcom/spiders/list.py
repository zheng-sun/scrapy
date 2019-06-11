# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from selenium import webdriver
import mofcom.items
from mofcom.Models.GetData import GetData
import time

class ListSpider(Spider):
    name = 'price_list'

    def __init__(self, *args, **kwargs):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(executable_path='D:\\PythonCode\\scrapy\\chromedriver_74.exe', chrome_options=chrome_options)
        #self.browser = webdriver.Chrome("E:\\PythonCode\\scrapy\\chromedriver_73.exe")
        self.browser.set_page_load_timeout(120)

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
        if file in para:
            if para[file] is not None:
                return para[file]
        return ''

    # start_urls = ['http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=13079&craft_index=13233&par_p_index=35']
    # self.crawler.engine.close_spider(self, '计数超过10，停止爬虫!')
    def start_requests(self):
        self.logger.info("start_requests %s", self.name)
        start_urls = GetData().getReptile({"code": '0', "spider_name": 'price_list'})
        for url in start_urls:
            yield Request(url=url['url'], callback=self.parse)

    def parse(self, response):
        self.logger.info("response url:%s", response.url)
        region_id = self.getParam(response.url, 'par_p_index')
        table = response.xpath('//table[@class="table-01 mt30"]/tbody/tr')
        for tr in table:
            tds = tr.xpath('td')
            if len(tds) > 0:
                ProductPriceHistoryItem = mofcom.items.ProductPriceHistoryItem()
                ProductPriceHistoryItem['date'] = tds[0].xpath('text()').extract_first()
                ProductPriceHistoryItem['product'] = tds[1].xpath('span/text()').extract_first()
                ProductPriceHistoryItem['price'] = tds[2].xpath('span/text()').extract_first()
                ProductPriceHistoryItem['unit'] = tds[2].xpath('text()').extract_first()
                ProductPriceHistoryItem['market'] = tds[3].xpath('a/text()').extract_first()
                ProductPriceHistoryItem['region_id'] = region_id
                yield ProductPriceHistoryItem

        #  请求下一页
        next_button = response.xpath('//a[@class="next"]').extract()
        if len(next_button) > 0:
            page = self.getParam(response.url, 'page')
            if page == '': #page为空，第一页
                next_page = response.url + '&page=2'
            else:  #page不为空，页码 + 1
                if int(page) > 9:
                    next_page = response.url[:-2] + str(int(page) + 1)
                elif int(page) > 99:
                    next_page = response.url[:-3] + str(int(page) + 1)
                else:
                    next_page = response.url[:-1] + str(int(page) + 1)
            yield Request(next_page, callback=self.parse)
        else:  #本页抓取完成,开启下一页
            self.logger.info("succes response url:%s", response.url)
            start_urls = GetData().getReptile({"code": '0', "spider_name": 'price_list'})
            if start_urls is not False:
                for url in start_urls:
                    yield Request(url=url['url'], callback=self.parse)
            else:
                self.crawler.engine.close_spider(self, 'price_list 地址抓取完成, 停止爬虫!')

            # 存入下一页地址
            # ReptileUrlItem = mofcom.items.ReptileUrlItem()
            # ReptileUrlItem['spider_name'] = 'price_list'
            # ReptileUrlItem['url'] = next_page
            # ReptileUrlItem['code'] = '0'
            # yield ReptileUrlItem







