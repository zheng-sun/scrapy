import pymysql
import pymysql.cursors
from DBUtils.PooledDB import PooledDB
import threading

# 连接数据库
connect = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    db='kaola',
    user='root',
    passwd='root',
    charset='utf8',
    use_unicode=True
)
# 通过cursor 执行sql
cursor = connect.cursor()

def tsk1():
    while True:
        print('运行tsk1')
        sql = """select * from good_comment"""
        cursor.execute(sql, )
        connect.commit()

def tsk2():
    while True:
        print('运行tsk2')
        sql = """select commentContent from good_comment"""
        cursor.execute(sql, )
        connect.commit()

tsk1()

# 创建并启动第一个线程
# t1 =threading.Thread(target=tsk1)
# t1.start()
# # 创建并启动第二个线程
# t2 =threading.Thread(target=tsk2)
# t2.start()
print('主线程执行完成!')

