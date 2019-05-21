# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from mofcom.items import CategoryItem, ProductItem, RegionItem, MarkerItem, ProductPriceHistoryItem, ReptileUrlItem
from mofcom.Models.Add import Add

class MofcomPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, CategoryItem):
            # 商品信息入库
            Add().insertCategory(item)
        elif isinstance(item, ProductItem):
            # 商品信息入库
            Add().insertProduct(item)
        elif isinstance(item, RegionItem):
            # 商品信息入库
            Add().insertRegoin(item)
        elif isinstance(item, MarkerItem):
            # 商品信息入库
            Add().insertMarket(item)
        elif isinstance(item, ProductPriceHistoryItem):
            # 商品信息入库
            Add().insertProductPriceHistory(item)
        elif isinstance(item, ReptileUrlItem):
            # 商品信息入库
            Add().insertReptile(item)
        return item
