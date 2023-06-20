import os, sys
sys.path.append(os.getcwd())

from jsonpath import jsonpath
# from loguru import logger
from tools.handle_log import *
from tools.handle_global_data import GDdata
from settings import testenvironment_dir


def extract_data_from_response(resp_dict, exctract_str, globle_data_obj, extract_id=1):
    """
    从响应结果当中，提取对应的值，并设置为全局变量(GlobalData类)。
    :param resp_dict: 请求之后的响应结果，字典类型。
    :param extract_str: 从excel当中读取的提取表达式字符串。
                        例如：{"token":"$..token"},{"officeType":"$..officeType"}
    :param globle_data_obj: 全局变量的实例化对象,由测试类生成对象。
    :param extract_id: 从excel获取。
    :return: None
    """
    logger.info("=============开始提取数据，从响应结果当中==============")

    # 优化--从响应中提取多个值，并设置为环境变量
    # 1- 将字符串转为数组
    extract_array = exctract_str.split(',')

    # 2- 循环读取数组中的元素，并赋值给extract_dict
    for value_extract in extract_array:

        # 1- 将表达式从字符串转化为字典
        extract_dict = eval(value_extract)
        print(extract_dict)

        # 将环境url：testenvironment_dir设置为全局变量
        url = str(testenvironment_dir)
        setattr(globle_data_obj, "url", url)

        # 2- 遍历字典,完成数据提取替换
        for key, jsonpath_expr in extract_dict.items():
            # 3-1 key变量名，value是jsonpath表达式
            logger.info(f"变量名为{key},获取的jsonpath表达式为{jsonpath_expr}",)
            # 3-2 使用jsonpath表达式提取"token"，获取到是个列表，否则返回False
            result_list = jsonpath(resp_dict, jsonpath_expr)
            logger.info(f"提取后的结果为：{result_list}")
            # 判断填写的extractid是否符合规则

            # 3-2 如果jsonpath取到了值，则设置为全局变量
            if result_list:
                logger.info("设置为GlobalData实例对象的属性和值...")
                try:
                    setattr(globle_data_obj, key, result_list[(extract_id-1)])
                    logger.info(f"全局变量名{key}，值为{getattr(globle_data_obj, key)}")
                except Exception:
                    logger.exception("请校验extract_id")
            else:
                logger.warning("没有取到值！")


if __name__ == '__main__':
    resp_dict = {
        "data": {
            "boxToken": None,
            "dimission": False,
            "inWhiteList": False,
            "isScan": None,
            "isSubscribe": None,
            "jwtTokenDTO": {
                "expireTime": 1682674313116,
                "refreshToken": "eyJhbGciOiJIUzI1NiJ9.eyJvZmZpY2VfaWQiOiIzMTRFRUUzREM4NzUxMUVEODY2NTBDNDJBMUI3QzUyNiIsImRldmljZVR5cGUiOiJkZWZhdWx0Iiwib2ZmaWNlX25hbWUiOiLotKLliqHliIbphY3kuJPnlKjlvovmiYB0ZXN0IiwidXNlcl90eXBlIjoiQSIsInVzZXJfaWQiOiIzMTUzQjREQ0M4NzUxMUVEODY2NTBDNDJBMUI3QzUyNiIsImxvZ2luVHlwZSI6IjIiLCJ1c2VyX25hbWUiOiLlvKDlgKkiLCJpc3MiOiJpTGF3LmNvbSIsImV4cCI6MTY4NDY2MTUxMzA3MSwiaWF0IjoxNjgyMDY5NTEzMDcxLCJvZmZpY2VUeXBlIjoiaW50ZWdyYXRpb24ifQ.NLK-A0lRyqbxyCORe6i3ds6Syq06X59FcPS18a1Oqos",
                "refreshTokenExpireTime": 1684661513116,
                "refreshTokenStartTime": 1682069513116,
                "startTime": 1682069513116,
                "token": "eyJhbGciOiJIUzI1NiJ9.eyJvZmZpY2VfaWQiOiIzMTRFRUUzREM4NzUxMUVEODY2NTBDNDJBMUI3QzUyNiIsImRldmljZVR5cGUiOiJkZWZhdWx0Iiwib2ZmaWNlX25hbWUiOiLotKLliqHliIbphY3kuJPnlKjlvovmiYB0ZXN0IiwidXNlcl90eXBlIjoiQSIsInVzZXJfaWQiOiIzMTUzQjREQ0M4NzUxMUVEODY2NTBDNDJBMUI3QzUyNiIsImxvZ2luVHlwZSI6IjIiLCJ1c2VyX25hbWUiOiLlvKDlgKkiLCJpc3MiOiJpTGF3LmNvbSIsImV4cCI6MTY4MjY3NDMxMzA3MSwiaWF0IjoxNjgyMDY5NTEzMDcxLCJvZmZpY2VUeXBlIjoiaW50ZWdyYXRpb24ifQ.bq__-9ICWuv0IHD4r_av3WkclDnObFNRjeCmW8Zuor8"},
            "officeName": "财务分配专用律所test",
            "officeType": "integration",
            "sessionKey": None,
            "unionId": None,
            "userDTO": {
                "avatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/Ca0fvluftpkX43gAibicDhoMh1pqp8wiaNDfK5j3rHhQFBiaHLMbv97ueX7H5FlLgVJrRrdr3O2ibTx2R5IWeXv6icaA/132",
                "deleted": 0,
                "email": "15032847575@163.com",
                "id": "3153B4DCC87511ED86650C42A1B7C526",
                "ifFollow": None,
                "name": "张倩",
                "officeId": "314EEE3DC87511ED86650C42A1B7C526",
                "phone": "15032161836",
                "pinyin": "zhangqian",
                "status": 1,
                "title": "",
                "userType": "A",
                "zone": "0086"},
            "verified": True},
        "isSuccess": True,
        "resultMsg": "执行成功！"}
    exctract_str = '{"token":"$..token"},{"officeType":"$..officeType"}'
    globle_data_obj = GDdata()
    extract_id = 1
    extract_data_from_response(resp_dict, exctract_str, globle_data_obj, extract_id)
