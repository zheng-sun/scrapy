# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 地址信息
class KaolaUrlLogItem(scrapy.Item):
    # 地址
    url = scrapy.Field()
    # 地址类型
    type = scrapy.Field()

# 分类信息
class KaolaCategoryItem(scrapy.Item):
    # 分类id
    categoryId = scrapy.Field()
    # 上级分类id
    parentId = scrapy.Field()
    # 分类级别
    categoryLevel = scrapy.Field()
    # 分类名称
    categoryName = scrapy.Field()
    # 分类状态
    categoryStatus = scrapy.Field()

# 品牌信息
class KaolaBrandItem(scrapy.Item):
    branch_id = scrapy.Field()
    branch_name = scrapy.Field()
    pass

# 商品基础信息
class KaolaGoodItem(scrapy.Item):
    #商品id
    good_id = scrapy.Field()
    # 商品名称
    name = scrapy.Field()
    # 产地(原产国)
    orig_country = scrapy.Field()
    # 品牌
    brand = scrapy.Field()
    # 售价
    currentPrice = scrapy.Field()
    # 参考价
    marketPrice = scrapy.Field()
    # 税费
    #taxAmoun = scrapy.Field()


# 商品评论信息
class KaolaGoodCommentItem(scrapy.Item):
    #商品id
    good_id = scrapy.Field()
    # 评论id
    goodsCommentId = scrapy.Field()
    # 评论设备
    appType = scrapy.Field()
    # 订单id
    orderId = scrapy.Field()
    # 用户名
    account_id = scrapy.Field()
    # 星级
    point = scrapy.Field()
    # 评论内容
    commentContent = scrapy.Field()
    # 评论时间
    createTime = scrapy.Field()
    #  修改时间
    updateTime = scrapy.Field()
    #  点赞数
    zanCount = scrapy.Field()
