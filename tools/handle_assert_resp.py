from jsonpath import jsonpath
from tools.handle_replace import replace_mark_by_data
# from loguru import logger
from tools.handle_log import *

def check_response(check_response_str, resp_dict, globle_data_obj=None):
    """
    :param check_response_str: Excel中读取的出来的，check_response列中的数据
                                举例：ss = '[{"expr":"$..userId","expected":False,"comp_type":"!="},' \
                                 '{"expr":"$..nickName","expected":["#new_phone#"],"comp_type":"=="}' \']'
                                 请注意：
                                        "expected":中如果是对比实际数据，则需加上列表符号[]，因为jsonpath提取出来的是个列表
    :param resp_dict: 接口返回值
    :return:
    """
    logger.info("================开始响应结果断言=================")
    # 1-替换 占位符"#字段名#”
    check_response_str = replace_mark_by_data(
        check_response_str, globle_data_obj)
    logger.info(f"要断言的数据为:{check_response_str}")

    # 2-将excel中的表达式从字符串转化为字典
    check_response_list = eval(check_response_str)

    # 3-循环读取数据，json表达式读取数据
    for one_check_response_dict in check_response_list:
        logger.info(f"比对类型为：{one_check_response_dict['comp_type']}")

        # 3-1 使用jsonpath提取数据，要么是列表，要么是False
        logger.info(f"jsonpath表达式为:{one_check_response_dict['expr']}")
        actual_result = jsonpath(resp_dict, one_check_response_dict['expr'])
        logger.info(f"实际结果为:{actual_result}")

        # 3-2 根据类型不同assert,拿实际结果与期望结果比对
        logger.info(f'期望结果为：{one_check_response_dict["expected"]}')
        if one_check_response_dict["comp_type"] == "!=":
            assert one_check_response_dict["expected"] != actual_result
        elif one_check_response_dict["comp_type"] == "==":
            assert one_check_response_dict["expected"] == actual_result
        else:
            logger.error(
                f'比对类型写错了，暂不支持 {one_check_response_dict["comp_type"]} 比对类型。')
            assert False


if __name__ == '__main__':
    ss = '[{"expr":"$..email","expected":["15032847575@163.com"],"comp_type":"=="}]'
    resp_dict = {
        "data": {
            "boxToken": None,
            "dimission": False,
            "inWhiteList": False,
            "isScan": None,
            "isSubscribe": None,
            "jwtTokenDTO": {
                "expireTime": 1682821744990,
                "refreshToken": "eyJhbGciOiJIUzI1NiJ9.eyJvZmZpY2VfaWQiOiIzMTRFRUUzREM4NzUxMUVEODY2NTBDNDJBMUI3QzUyNiIsImRldmljZVR5cGUiOiJkZWZhdWx0Iiwib2ZmaWNlX25hbWUiOiLotKLliqHliIbphY3kuJPnlKjlvovmiYB0ZXN0IiwidXNlcl90eXBlIjoiQSIsInVzZXJfaWQiOiIzMTUzQjREQ0M4NzUxMUVEODY2NTBDNDJBMUI3QzUyNiIsImxvZ2luVHlwZSI6IjIiLCJ1c2VyX25hbWUiOiLlvKDlgKkiLCJpc3MiOiJpTGF3LmNvbSIsImV4cCI6MTY4NDgwODk0NDkzOSwiaWF0IjoxNjgyMjE2OTQ0OTM5LCJvZmZpY2VUeXBlIjoiaW50ZWdyYXRpb24ifQ.yJFPSu8YX9fQjma_qoE7cl3r9u6F3UVyg4L_I_jp1Ng",
                "refreshTokenExpireTime": 1684808944990,
                "refreshTokenStartTime": 1682216944990,
                "startTime": 1682216944990,
                "token": "eyJhbGciOiJIUzI1NiJ9.eyJvZmZpY2VfaWQiOiIzMTRFRUUzREM4NzUxMUVEODY2NTBDNDJBMUI3QzUyNiIsImRldmljZVR5cGUiOiJkZWZhdWx0Iiwib2ZmaWNlX25hbWUiOiLotKLliqHliIbphY3kuJPnlKjlvovmiYB0ZXN0IiwidXNlcl90eXBlIjoiQSIsInVzZXJfaWQiOiIzMTUzQjREQ0M4NzUxMUVEODY2NTBDNDJBMUI3QzUyNiIsImxvZ2luVHlwZSI6IjIiLCJ1c2VyX25hbWUiOiLlvKDlgKkiLCJpc3MiOiJpTGF3LmNvbSIsImV4cCI6MTY4MjgyMTc0NDkzOSwiaWF0IjoxNjgyMjE2OTQ0OTM5LCJvZmZpY2VUeXBlIjoiaW50ZWdyYXRpb24ifQ.qEcGzMqYvH2xrhbAypyFaDffVhWD5_1ipREkF5cILUA"
            },
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
                "zone": "0086"
            },
            "verified": True
        },
        "isSuccess": True,
        "resultMsg": "执行成功！"
    }
    check_response(ss, resp_dict)
