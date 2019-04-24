# -*- coding: utf-8 -*-
import scrapy
import requests
import json
import kaola.items
#import KaolaGoodItem

#  获取评论 https://goods.kaola.com/commentAjax/comment_list_new.json?goodsId=1301389
#  获取品牌，分类 https://goods.kaola.com/product/breadcrumbTrail/1301389.json
#  获取商品价格，活动信息  https://goods.kaola.com/product/getPcGoodsDetailDynamic.json?goodsId=1301389
#  推荐商品   https://goods.kaola.com/product/getGoodsRecommendInfo.json?goodsId=1301389&accountId=&recommendType=5&t=1555493105258
#  考拉分类品牌接口 https://search.kaola.com/api/getFrontCategory.shtml

class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['search.kaola.com','goods.kaola.com']
    #start_urls = ['https://search.kaola.com/category/1472/2639.html?key=&pageSize=60&pageNo=1&sortfield=0&isStock=false&isSelfProduct=false&isPromote=false&isTaxFree=false&factoryStoreTag=-1&isCommonSort=false&isDesc=true&b=&proIds=&source=false&country=&needBrandDirect=false&isNavigation=0&lowerPrice=-1&upperPrice=-1&backCategory=&headCategoryId=&changeContent=crumbs_country&#topTab']
    #start_urls = ['https://search.kaola.com/category/1472.html']
    start_urls = ['https://search.kaola.com/api/getFrontCategory.shtml']

    def parse(self, response):
        dict_json = json.loads(response.body)
        frontCategoryList = dict_json['body']['frontCategoryList']

        for categroy in self.handle_children_node_list(frontCategoryList):
            yield categroy

        # # 获取搜索下商品列表
        # hreflist = response.xpath('//div[@class="goodswrap promotion"]/a/@href').extract()
        # for href in hreflist:
        #     yield scrapy.Request(response.urljoin(href), callback=self.parse_good, dont_filter=False)

        # # 搜索页下一页抓取
        # next_page = response.xpath('//div[@class="splitPages"]/a[@class="nextPage"]/@href').extract_first()
        # if next_page is not None:
        #     yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def handle_children_node_list(self, datalist):
        for data in datalist:
            Categoryitem = kaola.items.KaolaCategoryItem()
            Categoryitem['categoryId'] = data['categoryId']
            Categoryitem['parentId'] = data['parentId']
            Categoryitem['categoryLevel'] = data['categoryLevel']
            Categoryitem['categoryName'] = data['categoryName']
            Categoryitem['categoryStatus'] = data['categoryStatus']
            yield Categoryitem

            # 迭代下一层
            if 'childrenNodeList' in data:
                for categorys in self.handle_children_node_list(data['childrenNodeList']):
                    yield categorys

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
        yield scrapy.Request(apiUrl, callback=self.getGoodComment)

        # 获取推荐商品信息
        RecommendGoodUrls = response.xpath('//div[@id="j-listsimilar"]/div/div/a/@href').extract()
        for GoodUrl in RecommendGoodUrls:
            yield scrapy.Request(response.urljoin(GoodUrl), callback=self.parse_good, dont_filter=False)

    # 通过请求id截取商品id
    def good_url_split(self, goodUrl):
        goodUrlList = goodUrl.split('/')
        goodidList = goodUrlList[4].split('.')
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

    # 获取商品评论
    def getGoodComment(self, response):
        dict_json = json.loads(response.body)
        commentPage = dict_json['data']['commentPage']
        if commentPage['totalCount'] > 0:
            good_comment_item = kaola.items.KaolaGoodCommentItem()
            for result in commentPage['result']:
                good_comment_item['good_id'] = result['goodsId']
                good_comment_item['goodsCommentId'] = result['goodsCommentId']
                good_comment_item['appType'] = result['appType']
                good_comment_item['orderId'] = result['orderId']
                good_comment_item['account_id'] = result['accountId']
                good_comment_item['point'] = result['commentPoint']
                good_comment_item['commentContent'] = result['commentContent']
                good_comment_item['createTime'] = result['createTime']
                good_comment_item['updateTime'] = result['updateTime']
                good_comment_item['zanCount'] = result['zanCount']
                yield good_comment_item

            # 获取商品评论下一页数据
            if commentPage['pageNo'] < commentPage['totalPage']:
                good_id = dict_json['data']['commentStat']['goodsId']
                pageNo = commentPage['pageNo'] + 1

                pageNo = str(pageNo)
                good_id = str(good_id)

                apiUrl = 'https://goods.kaola.com/commentAjax/comment_list_new.json?goodsId=' + good_id + '&pageSize=100&pageNo='+ pageNo
                yield scrapy.Request(apiUrl, callback=self.getGoodComment)