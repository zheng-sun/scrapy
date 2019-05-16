from suning.Models.db import DB

class UrlLogModel(DB):

    # def __init__(self):
    #     self.cursor = db.initDB()

    # 爬取地址
    def insertUrlLog(self, item):
        sql = """replace into url_log (url, `title`, `type`, RefererUrl) values (%s, %s, %s, %s)"""
        self.cursor.execute(sql, (item['url'], item['title'], item['type'], item['RefererUrl']))
        self.connect.commit()