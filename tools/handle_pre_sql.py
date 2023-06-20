from tools.handle_replace import replace_mark_by_data
from tools.handle_mysql import MyMysql
from settings import database
from tools.handle_global_data import GDdata
# from loguru import logger
from tools.handle_log import *

def excute_pre_sql(pre_sql, globle_data_obj=None):
    logger.info("===========执行前置sql===========")
    # 1-数据替换
    pre_sql = replace_mark_by_data(pre_sql, globle_data_obj)

    # 2-将pre_sql从字符串转化为字典
    pre_sql_dict = eval(pre_sql)
    logger.info(f"将pre_sql从字符串转化为字典{pre_sql_dict}")

    # 3-连接数据库
    mysql = MyMysql(**database)
    logger.info("连接数据库成功！")

    # 4-循环遍历字典
    for key, sql_pha in pre_sql_dict.items():
        # 4-1 执行sql语句获取执行结果
        result_dict = mysql.get_query_sql_result(sql_pha)
        # 4-2 如果key不为空，则设置为全局变量
        if key != "" and result_dict is not None:
            setattr(GDdata, key, result_dict.get(key))
    mysql.close()


if __name__ == '__main__':
    pkId = '00008A59F4FA11E98AB27CD30AEB1494'
    setattr(GDdata, "pkId", pkId)
    pre_sql = '{"PKID":\'SELECT PKID from alpha_test.app_matter where PKID ="#pkId#"\'}'
    excute_pre_sql(pre_sql)
    if hasattr(GDdata, 'pkId'):
        print(GDdata, 'pkId')