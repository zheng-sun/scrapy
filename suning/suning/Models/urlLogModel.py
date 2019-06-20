from suning.Models.db import DB

class UrlLogModel(DB):

    # def __init__(self):
    #     self.cursor = db.initDB()

    def __del__(self):
        self.end()

    # 爬取地址
    def insertUrlLog(self, item):
        sql = """insert into spider_url_log (url, `title`, `type`, RefererUrl) values (%s, %s, %s, %s)"""
        # self.cursor.execute(sql, (item['url'], item['title'], item['type'], item['RefererUrl']))
        # self.connect.commit()
        self.update(sql, (item['url'], item['title'], item['type'], item['RefererUrl']))