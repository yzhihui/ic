import os
from settings import testdata_dir
from unittestreport import ddt, list_data
from tools.handle_my_excel import MyExcel
from testcase.base_case import BaseCase

# 1- 编写Excel测试数据--已完成并放入testdata测试数据层下

# 2- Excel数据读取（注意在写入参excel_path时，要写到具体文件）
excel_path = os.path.join(testdata_dir, "anli_cases.xlsx")   # 获取文件路径
me = MyExcel(excel_path, "案例库")  # 读取文件
case_list = me.read_all_datas()  # 将读取到的内容通过key，value的格式组成字典，存入列表


# 3-执行用例
@ddt
class QueryCase(BaseCase):
    @list_data(case_list)
    def test_cases(self, case):
        self.base_case(case)