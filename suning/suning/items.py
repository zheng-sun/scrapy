# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SuningCategoryItem(scrapy.Item):
    #  分类id
    CategoryId = scrapy.Field()
    #  分类名称
    CategoryName = scrapy.Field()
    #  上级id
    parentId = scrapy.Field()

class SuningUrlLogItem(scrapy.Item):
    #  爬取地址
    url = scrapy.Field()
    #  爬虫类型
    type = scrapy.Field()
    #  爬虫地址名称
    title = scrapy.Field()
    #  爬虫来源地址
    RefererUrl = scrapy.Field()

class SuningItem(scrapy.Item):
    pass
