# from loguru import logger
from tools.handle_log import *
import requests
from string import Template
import random
from settings import image_list
import warnings
from settings import testenvironment_dir


class HandleRequests():
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)

    def __init__(self) -> object:
        self.headers = {"Accept-Language": "zh-CN"}

    # 2- 发送请求处理（日志、请求、返回）
    def send_req(self, method, url, json=None, files=None, token=None):
        # 请求头处理：是否需要鉴权
        self.__pre_header(token)
        # headers = self.__pre_header(token)
        files = self.__pre_file(files)
        json = self.__pre_json(json)
        url = str(testenvironment_dir) + url
        logger.info("===================用例开始执行======================")
        logger.info(f"请求方式:{method}")
        logger.info(f"请求url:{url}")
        logger.info(f"请求json参数:{json}")
        logger.info(f"请求files参数:{files}")
        logger.info("开始发送请求........")
        logger.info(f"headers值为：{self.headers}")
        resp = requests.request(
            method,
            url=url,
            json=json,
            params=json,
            files=files,
            headers=self.headers)
        logger.info(f"响应状态码为：{resp.status_code}")
        return resp

    # 3- 定义私有化方法,单独处理鉴权
    def __pre_header(self, token):
        # headers = {'token': token}
        if token:
            logger.info("本条用例，需要token鉴权")
            # 请求头加上 Authorization
            headers_auth = {'token': token}    #
            resp = requests.request(
                "GET",
                str(testenvironment_dir) +
                "/ilaw/api/v2/documents/getToken",
                headers=headers_auth)
            authToken = resp.json()['authToken']
            self.headers.update({'Authorization': f'Token {authToken}'})  # 文件
            self.headers.update({'token': token})
            logger.info(f"本条用例header为{self.headers}")
        else:
            logger.info("本条用例，不需要鉴权。")

    # 4- files参数处理
    def __pre_file(self, files):
        """
        对如下形式的字符 {"file": ("$image_name", open("$image_path", "rb"))} 进行替换，转换成字典后返回
        :param files:从excel当中读出来的files字段
        :return:字典
        """
        if files and isinstance(files, str):
            logger.info(
                "==================有文件上传操作！需要替换文件名称和文件路径=========================")
            # 1-1 随机读取固定目录下随机
            image_name, image_path = image_list[random.randint(
                0, len(image_list) - 1)]
            # 1-2 使用Template模块进行替换操作
            template_old_str = Template(files)
            files = template_old_str.substitute(
                image_name=image_name, image_path=image_path)
            logger.info(f"文件名和文件路径替换后的结果为:\n{files}")
            files = eval(files)
        return files

    # 5-json参数处理
    def __pre_json(self, json_str):
        if json_str and isinstance(json_str, str):
            logger.info("本次请求，需要将从Excel中读取的字符串转为字典。")
            json_dict = eval(json_str)
            return json_dict
        return json_str
