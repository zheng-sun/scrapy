# kaola.models __init__
import pymysql
import pymysql.cursors

def __init__() :
    # 连接数据库
    connect = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        db='kaola',
        user='root',
        passwd='',
        charset='utf8',
        use_unicode=True
    )
    # 通过cursor 执行sql
    cursor = connect.cursor()