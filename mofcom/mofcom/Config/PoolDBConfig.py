import pymysql
import pymysql.cursors
from DBUtils.PooledDB import PooledDB

class DBPoolConfig(object):

    MYSQL_POOL = PooledDB(creator=pymysql,
                         maxconnections=5,
                         mincached=5,
                         maxcached=0,
                         blocking=True,
                         host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='root',
                         db='mofcom',
                         charset='utf8')