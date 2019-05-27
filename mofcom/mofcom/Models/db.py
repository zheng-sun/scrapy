import pymysql
import pymysql.cursors
from DBUtils.PooledDB import PooledDB
import traceback

class DB(object):
    # 连接池对象
    __pool = None

    def __init__(self):
        # 连接数据库
        self._conn = DB.db_connect()
        self._cursor = self._conn.cursor(cursor=pymysql.cursors.DictCursor)

        # self.connect = pymysql.connect(
        #     host='127.0.0.1',
        #     port=3306,
        #     db='mofcom',
        #     user='root',
        #     passwd='',
        #     charset='utf8',
        #     use_unicode=True
        # )
        # # 通过cursor 执行sql
        # self.cursor = self.connect.cursor(cursor=pymysql.cursors.DictCursor)
        # print('创建数据库连接')

    # 连接数据库
    @staticmethod
    def db_connect():
        if DB.__pool is None:
            __pool = PooledDB(creator=pymysql,
                              mincached=1,
                              maxcached=20,
                              host='127.0.0.1',
                              port=3306,
                              user='root',
                              passwd='root',
                              db='mofcom',
                              charset='utf8')
        return __pool.connection()

    # 查询所有数据
    def get_all(self, sql, param=None):
        try:
            if param is None:
                count = self._cursor.execute(sql)
            else:
                count = self._cursor.execute(sql, param)
            if count > 0:
                result = self._cursor.fetchall()
            else:
                result = False
            return result
        except Exception as e:
            traceback.print_exc(e)

    # 查询某一个数据
    def get_one(self, sql, param=None):
        try:
            if param is None:
                count = self._cursor.execute(sql)
            else:
                count = self._cursor.execute(sql, param)
            if count > 0:
                result = self._cursor.fetchone()
            else:
                result = False
            return result
        except Exception as e:
            traceback.print_exc(e)

    # 查询数量
    def get_count(self, sql, param=None):
        try:
            if param is None:
                count = self._cursor.execute(sql)
            else:
                count = self._cursor.execute(sql, param)
            return count
        except Exception as e:
            traceback.print_exc(e)

    # 查询部分
    def get_many(self, sql, param=None, num=0):
        try:
            if param is None:
                count = self._cursor.execute(sql)
            else:
                count = self._cursor.execute(sql, param)
            if count > 0:
                if num > 0:
                    result = self._cursor.fetchmany(num)
                else:
                    result = self._cursor.fetchall()
            else:
                return False
            return result
        except Exception as e:
            traceback.print_exc(e)

    # 插入一条数据
    def insert_one(self, sql, value):
        try:
            row_count = self._cursor.execute(sql, value)
            return row_count
        except Exception as e:
            traceback.print_exc(e)
            self.end("rollback")

    # 插入多条数据
    def insert_many(self, sql, values):
        try:
            row_count = self._cursor.executemany(sql, values)
            return row_count
        except Exception as e:
            traceback.print_exc(e)
            self.end("rollback")

    # 执行sql
    def __query(self, sql, param=None):
        try:
            if param is None:
                count = self._cursor.execute(sql)
            else:
                count = self._cursor.execute(sql, param)
            return count
        except Exception as e:
            traceback.print_exc(e)

    # 更新
    def update(self, sql, param=None):
        return self.__query(sql, param)

    # 删除
    def delete(self, sql, param=None):
        return self.__query(sql, param)

    def begin(self):
        self._conn.autocommit(0)

    def end(self, option='commit'):
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    # 关闭数据库连接,释放连接池资源
    def dispose(self, is_end=1):
        if is_end == 1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()