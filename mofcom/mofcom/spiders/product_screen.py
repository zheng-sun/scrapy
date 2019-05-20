# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from selenium import webdriver
import mofcom.items

class ProductScreenSpider(Spider):
    name = 'product_screen'
    #allowed_domains = ['nc.mofcom.gov.cn']
    #start_urls = ['']

    def __init__(self):
        #chrome_options = Options()
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--disable-gpu')
        #self.browser = webdriver.Chrome(executable_path='E:\\PythonCode\\scrapy\\chromedriver_73.exe"', chrome_options=chrome_options)
        #self.browser = webdriver.Chrome("D:\\PythonCode\\scrapy\\chromedriver_74.exe")
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
            category_id = par_craft_index_option.xpath('@value').extract_first()
            name = par_craft_index_option.xpath('text()').extract_first()
            if category_id is not '':
                CategoryItem = mofcom.items.CategoryItem()
                CategoryItem['category_id'] = category_id
                CategoryItem['name'] = name
                yield CategoryItem

                # 循环抓取下级农产品分类
                next_page = "http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=" + str(category_id)
                yield Request(url=next_page, callback=self.craft_index_parse)

        # 获取区域
        par_p_index_select = response.xpath('//select[@id="par_p_index"]/option')
        for par_p_index_option in par_p_index_select:
            region_id = par_p_index_option.xpath('@value').extract_first()
            name = par_p_index_option.xpath('text()').extract_first()
            if region_id is not '':
                RegionItem = mofcom.items.RegionItem()
                RegionItem['region_id'] = region_id
                RegionItem['name'] = name
                yield RegionItem

                # 获取区域下的市场
                next_page = "http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_p_index=" + str(region_id)
                yield Request(url=next_page, callback=self.p_index_parse)

    # 获取市场信息
    def p_index_parse(self, response):
        # url 截取出参数
        region_id = self.getParam(response.url, 'par_p_index')
        # 获取下级市场
        p_index_select = response.xpath('//select[@id="p_index"]/option')
        for p_index_option in p_index_select:
            market_id = p_index_option.xpath('@value').extract_first()
            name = p_index_option.xpath('text()').extract_first()
            if market_id is not '':
                MarkerItem = mofcom.items.MarkerItem()
                MarkerItem['market_id'] = market_id
                MarkerItem['name'] = name
                MarkerItem['region_id'] = region_id
                yield MarkerItem

    #  获取产品信息
    def craft_index_parse(self, response):
        # url 截取出参数
        category_id = self.getParam(response.url, 'par_craft_index')
        # 获取下级产品
        craft_index_select = response.xpath('//select[@id="craft_index"]/option')
        for craft_index_option in craft_index_select:
            product_id = craft_index_option.xpath('@value').extract_first()
            name = craft_index_option.xpath('text()').extract_first()
            if product_id is not '':
                ProductItem = mofcom.items.ProductItem()
                ProductItem['product_id'] = product_id
                ProductItem['name'] = name
                ProductItem['category_id'] = category_id
                yield ProductItem


