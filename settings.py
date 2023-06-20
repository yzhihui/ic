import os
# =========================项目框架路径配置===========================
# 1-项目框架路径
basedir = os.path.dirname(os.path.abspath(__file__))
# print(basedir)

# 2-测试数据路径
testdata_dir = os.path.join(basedir, "testdata")

# 3-测试用例路径
testcase_dir = os.path.join(basedir, "testcase")
print(testcase_dir)

# 4-测试报告路径
testreport_dir = os.path.join(basedir, "outputs", "reports")

# 5-测试执行日志路径
testlog_dir = os.path.join(basedir, "outputs", "logs")

# 6-测试图片路径
testupload_dir = os.path.join(basedir, "upload_images")

# 7-环境配置
testenvironment_dir = "https://test.alphalawyer.cn"


# ========================日志文件配置===========================
log_name = os.path.join(testlog_dir, "Alpha项-日志文件")
rotation = "100 MB"
retention = 10

# ========================数据库配置==============================
database = {
    "host": "rm-2ze2433x22ce09k6fto.mysql.rds.aliyuncs.com",
    "database": "alpha_test",
    "port": 3306,
    "user": "alpha_cs_test",
    "password": "8Z3NfIRdv6f5xeCN",
}


# ===================随机获取测试图片路径下的随机图片===================
image_list = []
for image_name in os.listdir(testupload_dir):
    image_list.append((image_name, os.path.join(testupload_dir, image_name)))
print(image_list)