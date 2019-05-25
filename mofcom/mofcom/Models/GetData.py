from mofcom.Models.db import DB

class GetData(DB):

    def __del__(self):
        self.dispose(1)

    def getCategory(self):
        sql = """select * from category"""
        return self.get_many(sql)
        # self.cursor.execute(sql)
        # return self.cursor.fetchall()

    def getProduct(self):
        sql = """select * from product"""
        return self.get_many(sql)
        # self.cursor.execute(sql)
        # return self.cursor.fetchall()

    def getRegion(self):
        sql = """select * from region"""
        return self.get_many(sql)
        # self.cursor.execute(sql)
        # return self.cursor.fetchall()

    def getMarket(self):
        sql = """select * from market"""
        return self.get_many(sql)
        # self.cursor.execute(sql)
        # return self.cursor.fetchall()

    def getReptile(self, param):
        sql = """select url from reptile where code = %s and spider_name = %s"""
        return self.get_many(sql, (param['code'], param['spider_name']), 1)
        # self.cursor.execute(sql, (code, spider_name))
        # return self.cursor.fetchall()

    def getReptileByUrl(self, param):
        sql = """select * from reptile where url = %s"""
        return self.get_count(sql, param)
        # self.cursor.execute(sql, ( url ))
        # return self.cursor.fetchone()

