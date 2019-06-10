import pymysql
import pymysql.cursors
from DBUtils.PooledDB import PooledDB
import threading
import time

class DB:

    __pool = None

    def __init__(self):
        # 连接数据库
        self._conn = DB.db_connect().connection()
        self._cursor = self._conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 连接数据库
    @staticmethod
    def db_connect():
        if DB.__pool is None:
            DB.__pool = PooledDB(creator=pymysql,
                              maxconnections=10,
                              mincached=10,
                              maxcached=10,
                              blocking=True,
                              host='127.0.0.1',
                              port=3306,
                              user='root',
                              passwd='root',
                              db='kaola',
                              charset='utf8')
        return DB.__pool

    def getSql1(self):
        print('查询getSql1')
        sql = """select * from good_comment"""
        self._cursor.execute(sql, )
        self._conn.commit()

    def getSql2(self):
        print('查询getSql2')
        sql = """select commentContent from good_comment"""
        self._cursor.execute(sql, )
        self._conn.commit()

def task1():
    while True:
        print('运行task1')
        DB().getSql1()
        time.sleep(1)


def task2():
    while True:
        print('运行task2')
        DB().getSql2()
        time.sleep(3)

# 创建并启动第一个线程
t1 =threading.Thread(target=task1)
t1.start()
# 创建并启动第二个线程
t2 =threading.Thread(target=task2)
t2.start()
print('主线程执行完成!')

