# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from selenium import webdriver


class JingdongSpider(Spider):
    name = 'jingdong'

    def __init__(self):
        self.browser = webdriver.PhantomJS("D:\\PythonCode\\scrapy\\phantomjs\\bin\\phantomjs.exe")
        self.browser.set_page_load_timeout(30)
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
        # driver.get("https://www.baidu.com")
        # print(driver.page_source)
        # driver.close()

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

