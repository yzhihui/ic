"""
    作用：定义python函数，用于数据替换
"""

import time
import uuid
from faker import Faker
from tools.handle_global_data import GDdata
# from loguru import logger
from tools.handle_log import *
__all__ = ["cur_time", "gen_uuid", "get_new_phone"]


# 1-随机生成13位时间戳
def cur_time():
    """
    :return: 生成13位时间戳
    """
    return str(int(time.time() * 1000))


# 2- 使用faker函数随机生成uuid
def gen_uuid():
    """
    :return: 生成uuid
    """
    return uuid.uuid4()

# 3-随机生成手机号码（中国）


def get_new_phone():
    """
    :param :
    :return:手机号
    """
    faker = Faker("zh-CN")
    phone = faker.phone_number()
    logger.info(f"随机生成的手机号为{phone}")
    # 设置为全局变量，便于其他接口访问
    setattr(GDdata, "new_phone", phone)
    return phone