# 1-导包
# from loguru import logger
from tools.handle_log import *
from settings import retention, rotation, log_name
from unittestreport import TestRunner
import unittestreport
from settings import testcase_dir, testreport_dir, testlog_dir
import unittest
import os
from tools.handle_send_message import *

# 2-主入口设置日志，写入日志文件
# logger.add(log_name,
#            rotation=rotation,
#            retention=retention,
#            compression="zip",
#            encoding="utf-8")

s = unittest.defaultTestLoader.discover(testcase_dir)

runner = unittestreport.TestRunner(s,
                                   filename="Alpha_test_report.html",
                                   report_dir=testreport_dir,
                                   title='Alpha项目-接口自动化测试报告',
                                   tester='system',
                                   desc="Alpha-接口自动化测试报告",
                                   templates=2
                                   )
runner.run(thread_count=3)

# 发送消息
result = runner.test_result
send_message(result)