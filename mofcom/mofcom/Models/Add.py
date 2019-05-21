from mofcom.Models.db import DB

class Add(DB):

    # 分类
    def insertCategory(self, item):
        sql = """replace into category (`category_id`, `name`) values (%s, %s)"""
        self.cursor.execute(sql, (item['category_id'], item['name']))
        self.connect.commit()

    # 商品
    def insertProduct(self, item):
        sql = """replace into product (`product_id`, `category_id`, `name`) values (%s, %s, %s)"""
        self.cursor.execute(sql, (item['product_id'], item['category_id'], item['name']))
        self.connect.commit()

    # 地区
    def insertRegoin(self, item):
        sql = """replace into region (`region_id`, `name`) values (%s, %s)"""
        self.cursor.execute(sql, (item['region_id'], item['name']))
        self.connect.commit()

    # 市场
    def insertMarket(self, item):
        sql = """replace into market ( `market_id`, `region_id`, `name`) values ( %s, %s, %s)"""
        self.cursor.execute(sql, (item['market_id'], item['region_id'], item['name']))
        self.connect.commit()

    # 商品价格历史
    def insertProductPriceHistory(self, item):
        sql = """replace into product_price_history ( `date`, `product`, `price`, `market`) values ( %s, %s, %s, %s)"""
        self.cursor.execute(sql, (item['date'], item['product'], item['price'], item['market']))
        self.connect.commit()

    # 地址
    def insertReptile(self, item):
        sql = """insert into reptile ( `url`, `code`) values ( %s, %s)"""
        self.cursor.execute(sql, (item['url'], item['code']))
        self.connect.commit()