# -*- coding: utf-8 -*-
import scrapy

#  获取评论 https://goods.kaola.com/commentAjax/comment_list_new.json?goodsId=1301389
#  获取品牌，分类 https://goods.kaola.com/product/breadcrumbTrail/1301389.json
#  获取商品价格，活动信息  https://goods.kaola.com/product/getPcGoodsDetailDynamic.json?goodsId=1301389
#  推荐商品   https://goods.kaola.com/product/getGoodsRecommendInfo.json?goodsId=1301389&accountId=&recommendType=5&t=1555493105258

class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['search.kaola.com']
    start_urls = ['http://search.kaola.com/']

    def parse(self, response):
        lists = response.xpath('//div[@class="goodswrap promotion"]').extract()
        for data in lists:
            yield {

            }
        #pass
