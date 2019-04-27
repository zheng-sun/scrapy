# -*- coding: utf-8 -*-
import scrapy
import json
import kaola.items

class GeturllogSpider(scrapy.Spider):
    name = 'getUrlLog'
    allowed_domains = ['search.kaola.com']
    start_urls = ['https://search.kaola.com/api/getFrontCategory.shtml']

    def parse(self, response):
        dict_json = json.loads(response.body)
        frontCategoryList = dict_json['body']['frontCategoryList']

        for categroy in self.handle_children_node_list(frontCategoryList):
            yield categroy

    #  迭代循环处分类信息
    def handle_children_node_list(self, datalist, parentId = 0, categoryId = 0):
        for data in datalist:
            Categoryitem = kaola.items.KaolaCategoryItem()
            Categoryitem['categoryId'] = data['categoryId']
            Categoryitem['parentId'] = data['parentId']
            Categoryitem['categoryLevel'] = data['categoryLevel']
            Categoryitem['categoryName'] = data['categoryName']
            Categoryitem['categoryStatus'] = data['categoryStatus']
            yield Categoryitem

            #  根据分类id  search 抓取商品数据
            if data['categoryLevel'] == 2:
                parentId = data['categoryId']

            if data['categoryLevel'] == 3:
                categoryId = data['categoryId']
                #  发送请求
                HttpsUrl = 'https://search.kaola.com/category/' + str(parentId) + '/' + str(categoryId) + '.html'
                UrlLogitem = kaola.items.KaolaUrlLogItem()
                UrlLogitem['url'] = HttpsUrl
                UrlLogitem['type'] = 'category'
                yield UrlLogitem
                #yield scrapy.Request(HttpsUrl, callback=self.parse_search_list)

            # 迭代下一层
            if 'childrenNodeList' in data:
                for categorys in self.handle_children_node_list(data['childrenNodeList'], parentId, categoryId):
                    yield categorys