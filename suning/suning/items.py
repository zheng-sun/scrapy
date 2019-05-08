# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SuningCategoryItem(scrapy.Item):
    CategoryId = scrapy.Field()
    CategoryName = scrapy.Field()
    parentId = scrapy.Field()

class SuningUrlLogItem(scrapy.Item):
    url = scrapy.Field()
    type = scrapy.Field()


class SuningItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
