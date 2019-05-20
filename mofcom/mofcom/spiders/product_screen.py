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
        self.browser = webdriver.Chrome("D:\\PythonCode\\scrapy\\chromedriver.exe")
        self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        print("spider closed")
        self.browser.close()

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
                break

    def craft_index_parse(self, response):
        #print(response.meta.get("par_crafe_index"))
        # 获取下级产品
        craft_index_select = response.xpath('//select[@id="craft_index"]/option')
        for craft_index_option in craft_index_select:
            craft_index_value = craft_index_option.xpath('@value').extract_first()
            craft_index_name = craft_index_option.xpath('text()').extract_first()
            if craft_index_value is not '':
                ParCraftIndexItem = mofcom.items.ParCraftIndexItem()
                ParCraftIndexItem['value'] = craft_index_value
                ParCraftIndexItem['name'] = craft_index_name
                ParCraftIndexItem['paradid'] = '0'
                yield ParCraftIndexItem

    # 截取请求地址获取参数
    def getParam(self, url, file):
        url_p = url.split('?')
        #if url

