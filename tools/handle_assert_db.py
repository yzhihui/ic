from tools.handle_replace import replace_mark_by_data
from tools.handle_mysql import MyMysql
from settings import database
# from loguru import logger
from tools.handle_log import *
from time import sleep


def assert_db(check_db_str, globle_data_obj=None):
    logger.info("============开始数据库断言==========")
    # 1-替换sql中的占位符-使用replace_mark_by_data
    one_db_assert_str = replace_mark_by_data(check_db_str, globle_data_obj)

    # 2- 转化为列表字典
    one_db_assert_list = eval(one_db_assert_str)

    # 3-实例化数据库
    mysql = MyMysql(**database)
    logger.info("连接数据库成功！")

    # 4-循环遍历断言列表，取出每一个断言字典
    for one_db_assert_dict in one_db_assert_list:
        logger.info(f"执行的sql语句为:{one_db_assert_dict.get('sql')}")
        if one_db_assert_dict.get("exe_type") == "count":
            sleep(5)
            result = mysql.get_count_query(one_db_assert_dict.get('sql'))
            logger.info(f"实际查询结果条数：{result}")
        else:
            result = ""
            logger.info(
                f"暂不支持的操作类型{one_db_assert_dict.get('count')},无法执行sql语句。。。。。。。")

        # 2-比对期望结果
        logger.info(f"期望结果为：{one_db_assert_dict.get('expected')}")
        try:
            assert result == one_db_assert_dict.get("expected")
        except BaseException:
            logger.exception("断言失败")
            raise
        else:
            logger.info("实际结果与预期相同，断言成功！")
        mysql.close()


if __name__ == '__main__':
    from tools.handle_global_data import GDdata
    setattr(GDdata, "PKID", "00008A59F4FA11E98AB27CD30AEB1494")
    ss = '[{"exe_type":"count","sql":\'SELECT * from alpha_test.app_matter where PKID ="#PKID#"\',"expected":1}]'
    replace_mark_by_data(ss)
    assert_db(ss)
