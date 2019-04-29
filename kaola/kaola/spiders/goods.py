# -*- coding: utf-8 -*-
import scrapy
import pymysql
import pymysql.cursors
import kaola.items
import json
import requests

class GoodsSpider(scrapy.Spider):
    name = 'goods'
    allowed_domains = ['goods.kaola.com']

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='kaola',
            user='root',
            passwd='',
            charset='utf8',
            use_unicode=True
        )
        # 通过cursor 执行sql
        self.cursor = self.connect.cursor()

    def updateUrlLogStatus(self, url):
        sql = """
            update url_log set `status` = 1 where `url` = %s
        """
        self.cursor.execute(sql, (url))
        self.connect.commit()

    def start_requests(self):
        while True:
            urls = self.getUrl()
            for url in urls:
                yield scrapy.Request(url, callback=self.parse_good, dont_filter=False)

    def getUrl(self):
        # 获取category 爬取地址
        sql = """select url from url_log where type = 'good' and status = 0 limit 1"""
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return_data = []
        for d in data:
            d_list = list(d)
            return_data.append(d_list[0])
            self.updateUrlLogStatus(d_list[0])
        return return_data

    # 商品信息
    def parse_good(self, response):
        good_item = kaola.items.KaolaGoodItem()
        # 截取商品id
        good_id = self.good_url_split(response.url)
        good_item['good_id'] = good_id

        # 获取商品价格
        good_price = self.getGoodMarkprice(good_id)
        good_item['marketPrice'] = good_price['marketPrice']
        good_item['currentPrice'] = good_price['currentPrice']
        good_item['name'] = response.xpath('//dt[@class="product-title"]/text()').extract_first()
        good_item['orig_country'] = response.xpath('//dt[@class="orig-country"]/span/text()').extract_first()
        good_item['brand'] = response.xpath('//dt[@class="orig-country"]/a/text()').extract_first()
        yield good_item

        # 获取商品评论信息
        apiUrl = 'https://goods.kaola.com/commentAjax/comment_list_new.json?goodsId='+good_id + '&pageSize=100'
        UrlLogitem = kaola.items.KaolaUrlLogItem()
        UrlLogitem['url'] = apiUrl
        UrlLogitem['type'] = 'good_comment'
        yield UrlLogitem
        #yield scrapy.Request(apiUrl, callback=self.getGoodComment)

        # 获取推荐商品信息
        RecommendGoodUrls = response.xpath('//div[@id="j-listsimilar"]/div/div/a/@href').extract()
        for GoodUrl in RecommendGoodUrls:
            UrlLogitem = kaola.items.KaolaUrlLogItem()
            UrlLogitem['url'] = GoodUrl
            UrlLogitem['type'] = 'good'
            yield UrlLogitem
            #yield scrapy.Request(response.urljoin(GoodUrl), callback=self.parse_good, dont_filter=False)

        # 获取商品品牌信息
        APIUrl = 'https://goods.kaola.com/product/breadcrumbTrail/'+ good_id +'.json'
        yield scrapy.Request(APIUrl, callback = self.parse_category)

    def parse_category(self, response):
        dict_json = json.loads(response.body)
        retdata = dict_json['retdata']
        good_id = self.good_url_split_good_category(response.url)

        # 品牌信息
        brandItem = kaola.items.KaolaBrandItem()
        brandItem['brandId'] = retdata['brandId']
        brandItem['brandName'] = retdata['brandName']
        yield brandItem

        #  商品品牌信息
        GoodBrandItem = kaola.items.KaolaGoodBrandItem()
        GoodBrandItem['good_id'] = good_id
        GoodBrandItem['brandId'] = retdata['brandId']
        yield GoodBrandItem

        for category in dict_json['retdata']['categoryList']:
            GoodCategoryItem = kaola.items.KaolaGoodCategoryItem()
            GoodCategoryItem['good_id'] = good_id
            GoodCategoryItem['categoryId'] = category['categoryId']
            GoodCategoryItem['categoryName'] = category['categoryName']
            GoodCategoryItem['level'] = category['level']
            GoodCategoryItem['leaf'] = category['leaf']
            yield GoodCategoryItem

    # 通过请求id截取商品id
    def good_url_split(self, goodUrl):
        goodUrlList = goodUrl.split('/')
        goodidList = goodUrlList[4].split('.')
        good_id = goodidList[0]
        return good_id

    def good_url_split_good_category(self, goodUrl):
        goodUrlList = goodUrl.split('/')
        goodidList = goodUrlList[5].split('.')
        good_id = goodidList[0]
        return good_id

    # 获取商品价格
    def getGoodMarkprice(self, goodId):
        params = {'goodsId': goodId}
        apiUrl = 'https://goods.kaola.com/product/getPcGoodsDetailDynamic.json'
        res = requests.get(apiUrl, params=params)
        json_requests = res.content.decode()
        dict_json = json.loads(json_requests)

        return_dict = {}
        marketPrice = dict_json['data']['skuPrice']['marketPrice']
        return_dict['marketPrice'] = marketPrice
        currentPrice = dict_json['data']['skuPrice']['currentPrice']
        return_dict['currentPrice'] = currentPrice
        return return_dict