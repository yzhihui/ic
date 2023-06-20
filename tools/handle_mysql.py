import pymysql


class MyMysql:
    def __init__(self, host, database, user, password, port=3306):
        try:
            # 1、连接数据库
            self.con = pymysql.connect(
                host=host,
                database=database,
                port=port,
                user=user,
                password=password,
                # 一行数据是字典形式。多行数据是列表中嵌套字典.
                cursorclass=pymysql.cursors.DictCursor
            )
        except BaseException:
            raise
        else:
            # 2、创建游标
            self.cur = self.con.cursor()

    def get_count_query(self, select_sql, args=None):
        count = self.cur.execute(select_sql, args)
        return count

    def get_query_sql_result(self, select_sql, args=None, size=1):
        """
        :param select_sql: 查询sql语句
        :param args: sql语句的参数，参看self.cur.execute的函数说明。
        :param size: =1,表示fetchone,=-1,表示fetchall，>1,表示fetchmany
        :return: 查询结果
        """
        self.cur.execute(select_sql, args)
        if size == 1:
            return self.cur.fetchone()
        elif size == -1:
            return self.cur.fetchall()
        elif size > 1:
            return self.cur.fetchmany(size)

    def close(self):
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    sql_tuple = ("rm-2ze2433x22ce09k6fto.mysql.rds.aliyuncs.com",
                 "alpha_test", "alpha_cs_test", "8Z3NfIRdv6f5xeCN", 3306)
    mmsql = MyMysql(*sql_tuple)
    res = mmsql.get_query_sql_result(
        'SELECT * FROM alpha_test.app_matter WHERE PKID ="00008A59F4FA11E98AB27CD30AEB1494";')
    print(res)
    mmsql.close()
