import pymysql
import pymysql.cursors
from DBUtils.PooledDB import PooledDB
import threading

class DB:
    def __init__(self):
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='kaola',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True
        )
        # 通过cursor 执行sql
        self.cursor = self.connect.cursor()

    def getSql1(self):
        print('查询getSql1')
        sql = """select * from good_comment"""
        self.cursor.execute(sql, )
        self.connect.commit()

    def getSql2(self):
        print('查询getSql2')
        sql = """select commentContent from good_comment"""
        self.cursor.execute(sql, )
        self.connect.commit()

def task1():
    while True:
        print('运行task1')
        DB().getSql1()

def task2():
    while True:
        print('运行task2')
        DB().getSql2()

# 创建并启动第一个线程
t1 =threading.Thread(target=task1)
t1.start()
# 创建并启动第二个线程
t2 =threading.Thread(target=task2)
t2.start()
print('主线程执行完成!')

