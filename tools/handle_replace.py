"""
  1- 使用正则表达式 提取需要替换的字段
  2- 遍历列表完成替换
"""
import re
from tools.handle_global_data import GDdata
import time
# from loguru import logger
from tools.handle_log import *
from tools import handle_data


def replace_mark_by_data(req_data, globle_data_obj=None):
    """
    完成请求参数中的占位符（#参数#）的数据替换，返回替换后的请求数据
    :param req_data: excel中的字符窜
    :param globle_data_obj: 全局变量实例化，给测试类传参
    :return: 替换完占位符后的数据
    """
    logger.info("=====================开始进行替换操作=======================")
    # 1) 使用正则表达式 提取需要替换的占位符
    result = re.findall("#(\\w+?)#", req_data)   # 匹配到全部返回（列表），未匹配到返回空列表
    # 2) 列表去重
    to_be_replace_mark = list(set(result))
    if to_be_replace_mark == []:
        logger.info("不需要替换操作")
        return req_data
    # 3) 循环遍历列表，判断是否在 全局变量里，存在替换，不存在，判断是否在python函数中可匹配，存在替换，不存在返回未匹配到
    for key in to_be_replace_mark:
        logger.info(f"当前要处理的占位符为{key}")
        if hasattr(globle_data_obj, key):
            logger.info(f"需要替换的值{key}在全局变量GDdata中存在,开始替换操作。。。。")
            req_data = req_data.replace(
                f"#{key}#", str(
                    getattr(
                        globle_data_obj, key)))
        else:
            logger.info(f"需要替换的值{key}不在全局变量globle_data_obj中，在Python函数中寻找。。。。")
            # 3-1) if key == 'cur_time'----改为通用============
            # 3-1) 解决方法：创建一个py文件（自定义__all__），函数名和字段保持一致，在调用的文件中使用getattr方法获取，之后使用
            #              字符串的replace方法进行数据替换
            if key in handle_data.__all__:
                real_value = getattr(handle_data, key)()
                logger.info(f"找到了，执行函数后的得到的值为{real_value}")
                req_data = req_data.replace(f"#{key}#", real_value)
            else:
                logger.info(
                    f"需要替换的值{key}在全局变量和python函数中均不存在,请检查标识符是否正确。。。。。。。")
    logger.info(f"替换后的值为：\n {req_data}")
    return req_data


if __name__ == '__main__':
    url = """{"#get_new_phone#"}"""
    replace_mark_by_data(url)
