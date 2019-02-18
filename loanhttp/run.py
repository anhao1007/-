# -*- coding:utf-8 -*- 
# @Time    :2019/1/2113:58
# @File    :.py
import unittest
import HTMLTestRunnerNew;
from class_loanhttp import files_os
#存储测试用例里的类
# suit=unittest.TestSuite();
# #加载测试用例
# load=unittest.TestLoader();
#注册用例
# suit.addTest(load.loadTestsFromTestCase(Test_Logig))
#登录用例
# suit.addTest(load.loadTestsFromTestCase(Test_Register))
#充值用例
# suit.addTest(load.loadTestsFromTestCase(Test_Recharg))
suit=unittest.defaultTestLoader.discover(files_os.test_case,pattern='test_*.py',top_level_dir=None)
with open(files_os.report_file,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file,tester='anhao')
    runner.run(suit);