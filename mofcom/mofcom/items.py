# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 分类
class CategoryItem(scrapy.Item):
    category_id = scrapy.Field()
    name = scrapy.Field()

# 产品
class ProductItem(scrapy.Item):
    product_id = scrapy.Field()
    category_id = scrapy.Field()
    name = scrapy.Field()

# 区域
class RegionItem(scrapy.Item):
    region_id = scrapy.Field()
    name = scrapy.Field()

# 市场
class MarkerItem(scrapy.Item):
    market_id = scrapy.Field()
    region_id = scrapy.Field()
    name = scrapy.Field()

# 商品价格历史
class ProductPriceHistoryItem(scrapy.Item):
    date = scrapy.Field()
    product = scrapy.Field()
    price = scrapy.Field()
    market = scrapy.Field()

class ReptileUrlItem(scrapy.Item):
    url = scrapy.Field()
    code = scrapy.Field()
