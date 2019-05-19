# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from selenium import webdriver
import mofcom.items

class ProductScreenSpider(Spider):
    name = 'product_screen'
    #allowed_domains = ['nc.mofcom.gov.cn']
    #start_urls = ['']

    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
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

    def start_requests(self):
        start_urls = ['http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml']
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        # 获取产品
        par_craft_index_select = response.xpath('//select[@id="par_craft_index"]/option')
        for par_craft_index_option in par_craft_index_select:
            par_craft_index_value = par_craft_index_option.xpath('@value').extract_first()
            par_craft_index_name = par_craft_index_option.xpath('text()').extract_first()
            if par_craft_index_value is not '':
                ParCraftIndexItem = mofcom.items.ParCraftIndexItem()
                ParCraftIndexItem['value'] = par_craft_index_value
                ParCraftIndexItem['name'] = par_craft_index_name
                ParCraftIndexItem['paradid'] = '0'
                yield ParCraftIndexItem

                # 循环抓取下级农产品分类
                next_page = "http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=" + str(par_craft_index_value)
                yield Request(url=next_page, callback=self.craft_index_parse)

        # 获取城市

    def craft_index_parse(self, response):
        # url 截取出参数
        par_craft_index_id = self.getParam(response.url, 'par_craft_index')
        # 获取下级产品
        craft_index_select = response.xpath('//select[@id="craft_index"]/option')
        for craft_index_option in craft_index_select:
            craft_index_value = craft_index_option.xpath('@value').extract_first()
            craft_index_name = craft_index_option.xpath('text()').extract_first()
            if craft_index_value is not '':
                ParCraftIndexItem = mofcom.items.ParCraftIndexItem()
                ParCraftIndexItem['value'] = craft_index_value
                ParCraftIndexItem['name'] = craft_index_name
                ParCraftIndexItem['paradid'] = par_craft_index_id
                yield ParCraftIndexItem


