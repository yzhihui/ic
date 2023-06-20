import os, sys
sys.path.append(os.getcwd()) #添加环境变量，实现跨文件调用（vscode使用）

from settings import testdata_dir
from unittestreport import ddt, list_data
from tools.handle_my_excel import MyExcel
from testcase.base_case import BaseCase

# 司法观点库
# 1- 编写Excel测试数据--已完成并放入testdata测试数据层下

# 2- Excel数据读取（注意在写入参excel_path时，要写到具体文件）
excel_path = os.path.join(testdata_dir, "judicialview_cases.xlsx")   # 获取文件路径
me = MyExcel(excel_path, "司法观点库")  # 读取文件
case_list = me.read_all_datas()  # 将读取到的内容通过key，value的格式组成字典，存入列表


# 3-执行用例
@ddt
class Judicialview(BaseCase):
    @list_data(case_list)
    def test_judicialview(self, case):
        self.base_case(case)
