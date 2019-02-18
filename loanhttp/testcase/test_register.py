# -*- coding:utf-8 -*- 
# @Time    :2019/1/2210:58
# @File    :.py
import unittest
from  ddt import ddt,data
from class_loanhttp.Do_excel import Do_Excel;
from class_loanhttp import files_os
from class_loanhttp.request import Methed;
from py_mysql.mysql import Mysql_operation;
import json
@ddt
class Test_Register(unittest.TestCase):
    do_excel=Do_Excel(files_os.case_file);
    read_login=do_excel.read('registered');#读取注册的测试用例数据
    resps=Methed()#实例化类
    def sq_query(self):#接受sql类查询的数据
        mysql=Mysql_operation()
        sql='select max(mobilephone)from future.member'
        max=mysql.query(sql)[0]
        max_1=max[0];
        return max_1
    @data(*read_login)
    def test_register(self,case):
       max_1=self.sq_query();#调用数据库查询的结果
       print("---第{}条用例开始执行:{}---".format(case.case_id,case.title));
       data_s=eval(case.datas)
       if data_s['mobilephone'] == '${r_mobile}':
           data_s['mobilephone']=int(max_1)+1
       resp=self.resps.request(case.methed,case.url,data_s)
       try:
           self.assertEqual(case.expectations,resp.text);
           TestResult='Pass';
       except AssertionError as e:
           TestResult = 'Failed';
           print('错误是{}'.format(e))
           raise e;
       finally:
          self.do_excel.write('registered',case.case_id+1,resp.text,TestResult)#写入数据
          print("---第{}条用例执行结束---结果是{}".format(case.case_id,TestResult));
    # @classmethod
    # def tearDownClass(cls):
    #     cls.mysql.close();