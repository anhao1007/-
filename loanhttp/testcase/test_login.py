# -*- coding:utf-8 -*- 
# @Time    :2019/1/219:35
# @File    :.py
import unittest
from  ddt import ddt,data
from class_loanhttp.Do_excel import Do_Excel;
from class_loanhttp import files_os
from class_loanhttp.request import Methed;

@ddt
class Test_Logig(unittest.TestCase):
    do_excel=Do_Excel(files_os.case_file);
    read_login=do_excel.read('login');#读取登录的测试用例数据
    resps=Methed()#实例化类
    @data(*read_login)
    def test_login(self,case):
       print("---第{}条用例开始执行：{}---".format(case.case_id,case.title));
       resp=self.resps.request(case.methed,case.url,case.datas)
       try:
           self.assertEqual(case.expectations,resp.text);
           TestResult='Pass';
       except AssertionError as e:
           TestResult = 'Failed';
           print('错误是{}'.format(e))
           raise e;
       finally:
          self.do_excel.write('login',case.case_id+1,resp.text,TestResult)#写入数据
          print("---第{}条用例执行结束---结果是{}".format(case.case_id,TestResult));

