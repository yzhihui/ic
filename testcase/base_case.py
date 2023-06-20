import json
import unittest
# from loguru import logger
from tools.handle_log import *
from tools.handle_replace import replace_mark_by_data
from tools.handle_requests import HandleRequests
from tools.handle_extract import extract_data_from_response
from tools.handle_global_data import GDdata
from tools.handle_response import transform_resp_text_to_json
from tools.handle_pre_sql import excute_pre_sql
from tools.handle_assert_db import assert_db
from tools.handle_assert_resp import check_response
from jsonpath import jsonpath

class BaseCase(unittest.TestCase):
    # 1-登录操作设置为类级别前置setupclass,headers后面都要用，设置为类属性
    @classmethod
    def setUpClass(cls) -> None:
        cls.hreq = HandleRequests()
        cls.globle_data = GDdata()

    def base_case(self, case):
        logger.info(f"===== 开始执行用例：{case['title']} ======")
        logger.info(f"测试数据:\n{case}")
        self.hreq.setUp()

        # 1- 执行前置sql
        if case.get("pre_sql"):
            excute_pre_sql(case.get("pre_sql"), self.globle_data)

        # 替换url中的占位符
        if case.get("url_type") == 1:
            case["url"] = replace_mark_by_data(
                case["url"],self.globle_data
            )
            logger.info(f"替换后的url为:{case['url']}")
        else:
            logger.info("本条case中无 url 参数 ，不需要判断是否需要替换。。。。。")

        # 2- 替换请求数据req_data字段中的占位符
        if case.get("req_data"):
            case["req_data"] = replace_mark_by_data(
                case["req_data"], self.globle_data)
        else:
            logger.info("本条case中无 req_data 参数 ，不需要判断是否需要替换。。。。。")

        # 3- token是否有值
        if hasattr(self.globle_data, "token"):
            # 是否需要循环调用
            while case.get("cycle_stop"):
                logger.info("========此条用例需要循环调用======")
                for i in range(30):
                    resp = self.hreq.send_req(
                        case["method"],
                        case["url"],
                        json=case["req_data"],
                        files=case["files"],
                        token=getattr(self.globle_data, "token")
                    )
                    # 判断指定字段为指定值时循环停止
                    cycle_stop = eval(case.get("cycle_stop"))
                    for k, v in cycle_stop.items():
                        real_v = jsonpath(resp.json(), "$.." + k)[0]
                        if int(real_v) == int(v):
                            logger.info(f"{k}的字段值为{real_v}，循环结束")
                            break
                    else:
                        continue
                    break
                else:
                    logger.info("已调用30次，未得到返回结果")
                break

            else:
                logger.info("========此条用例不需要循环调用======")
                resp = self.hreq.send_req(
                    case["method"],
                    case["url"],
                    json=case["req_data"],
                    files=case["files"],
                    token=getattr(self.globle_data, "token")
                )
        else:
            while case.get("cycle_stops"):
                logger.info("========此条用例需要循环调用======")
                for i in range(30):
                    resp = self.hreq.send_req(
                        case["method"],
                        case["url"],
                        json=case["req_data"],
                        files=case["files"]
                    )
                    # 判断指定字段为指定值时循环停止
                    cycle_stop = eval(case.get("cycle_stop"))
                    for k, v in cycle_stop.items():
                        real_v = jsonpath(resp.json(), "$.." + k)[0]
                        if int(real_v) == int(v):
                            logger.info(f"{k}的字段值为{real_v}，循环结束")
                            break
                    else:
                        continue
                    break
                else:
                    logger.info("已调用30次，未得到返回结果")
                break

            else:
                logger.info("========此条用例不需要循环调用======")
                resp = self.hreq.send_req(
                    case["method"],
                    case["url"],
                    json=case["req_data"],
                    files=case["files"]
                )

        # 4- 处理响应结果。如果它是一个字符串，要拼接成一个json串形式字符串。
        resp_dict = transform_resp_text_to_json(resp)
        logger.info(f"接口返回值转换为字典后的值为：{resp_dict}")

        # 5- 如果有提取-extract，就进行提取操作。并设置为全局变量
        if case.get("extract"):
            if case.get("extract_id"):
                extract_data_from_response(
                    resp_dict, case.get("extract"), self.globle_data, case.get("extract_id"))
            else:
                extract_data_from_response(
                    resp_dict, case.get("extract"), self.globle_data)
        else:
            logger.info("本条case无 extract 字段，不需要提取操作。。。。。")

        # 6- 响应结果断言
        if case.get("check_response"):
            check_response(
                case.get("check_response"),
                resp_dict,
                self.globle_data)
        else:
            logger.info("本条case无 check_response 字段，不需要断言。。。。。")

        # 7- 数据库断言
        if case.get("check_db"):
            assert_db(case.get("check_db"), self.globle_data)
        else:
            logger.info("本条case无 check_db 字段，不需要断言。。。。。")