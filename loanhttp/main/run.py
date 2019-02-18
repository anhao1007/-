# -*- coding:utf-8 -*- 
# @Time    :2019/1/2113:58
# @File    :.py

import unittest
import HTMLTestRunnerNew;
from testcase.test_login import Test_Logig;
from class_loanhttp import files_os
from testcase.test_register import Test_Register
from testcase.test_recharg import Test_Recharg

#存储测试用例里的类
suit=unittest.TestSuite();
#加载测试用例
load=unittest.TestLoader();
#注册用例
# suit.addTest(load.loadTestsFromTestCase(Test_Logig))
#登录用例
# suit.addTest(load.loadTestsFromTestCase(Test_Register))
#充值用例
suit.addTest(load.loadTestsFromTestCase(Test_Recharg))
with open(files_os.report_file,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file,tester='anhao')
    runner.run(suit);