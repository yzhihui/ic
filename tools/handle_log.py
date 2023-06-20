import logging
from settings import *

def log():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # 设置日志格式
    format1 = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    # 添加到文件
    fh = logging.FileHandler(testlog_dir + "/log.txt", 'a+', encoding="utf-8")
    fh.setFormatter(format1)
    logger.addHandler(fh)
    return logger

logger = log()