import pymysql
import pymysql.cursors

class DB(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='mofcom',
            user='root',
            passwd='',
            charset='utf8',
            use_unicode=True
        )
        # 通过cursor 执行sql
        self.cursor = self.connect.cursor()