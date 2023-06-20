import requests
# from loguru import logger
from tools.handle_log import *

def transform_resp_text_to_json(resp):
    """
    如果resp的响应数据，是json串，那么直接通过resp.json（）转成python对象
    如果resp的响应数据，不是json格式，则自动补全key为data，形式为 data：resp.text
    :param resp: 接口请求之后的Response对象
    :return: resp_dict
    """
    logger.info("=======开始处理响应数据，换成dict======")
    try:
        if isinstance(resp.json(), dict):
            logger.info("响应结果为key-value形式的json串，直接转换成dict")
            resp_dict = resp.json()
        else:
            logger.info("响应结果非key-value形式的，补全key")
            resp_dict = {"data": resp.text}
            logger.info(f"补全之后的字典为：{resp_dict}")
    except BaseException:
        resp_dict = {"data": resp.text}

    return resp_dict