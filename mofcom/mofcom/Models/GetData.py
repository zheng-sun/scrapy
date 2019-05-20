from mofcom.Models.db import DB

class GetData(DB):

    def getCategory(self):
        sql = """select * from category"""
        self.cursor.execute(sql)
        self.connect.commit()

    def getProduct(self):
        sql = """select * from product"""
        self.cursor.execute(sql)
        self.connect.commit()

    def getRegion(self):
        sql = """select * from region"""
        self.cursor.execute(sql)
        self.connect.commit()

    def getMarket(self):
        sql = """select * from market"""
        self.cursor.execute(sql)
        self.connect.commit()