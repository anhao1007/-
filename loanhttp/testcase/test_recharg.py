# -*- coding:utf-8 -*- 
# @Time    :2019/1/2215:47
# @File    :.py
import unittest
from  ddt import ddt,data
from class_loanhttp.Do_excel import Do_Excel;
from class_loanhttp import files_os
from class_loanhttp.request import Methed;
import json
@ddt
class Test_Recharg(unittest.TestCase):
    do_excel=Do_Excel(files_os.case_file);
    read_rech=do_excel.read('recharg');#读取充值的测试用例数据
    @classmethod
    def setUpClass(cls):
     cls.resps=Methed()#实例化类
    @data(*read_rech)
    def test_recharg(self,case):
       print("---第{}条用例开始执行:{}---".format(case.case_id,case.title));
       resp=self.resps.request(case.methed,case.url,case.datas)
       expect = case.expectations
       try:
           if expect=='None':#没实现
            self.assertEqual(expect,resp.json()['code']);
           else:
               self.assertEqual(str(expect), resp.json()['code']);
           TestResult = 'Pass';
       except AssertionError as e:
           TestResult = 'Failed';
           print('错误是{}'.format(e))
           raise e;
       finally:
          self.do_excel.write('recharg',case.case_id+1,resp.text,TestResult)#写入数据
          print("---第{}条用例执行结束---结果是{}".format(case.case_id,TestResult));