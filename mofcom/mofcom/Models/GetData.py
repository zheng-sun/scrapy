from mofcom.Models.db import DB

class GetData(DB):

    def getCategory(self):
        sql = """select * from category"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getProduct(self):
        sql = """select * from product"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getRegion(self):
        sql = """select * from region"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getMarket(self):
        sql = """select * from market"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getReptile(self, code, spider_name):
        sql = """select url from reptile where code = %s and spider_name = %s limit 32"""
        self.cursor.execute(sql, (code, spider_name))
        return self.cursor.fetchall()

    def getReptileByUrl(self, url):
        sql = """select * from reptile where url = %s"""
        self.cursor.execute(sql, ( url ))
        return self.cursor.fetchone()

