# -*- coding:utf-8 -*- 
# @Time    :2019/1/2114:35
# @File    :.py
import os
#测试数据的绝对路径
files=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));#项目根路径
datas=os.path.join(files,'datas');#定位到datas目录
case_file=os.path.join(datas,'loan_datas.xlsx')#定位到表

#配置文件的绝对路径
conf=os.path.join(files,'conf')#定位到conf目录
conf_file=os.path.join(conf,'loan_http.conf');

#测试报告文件的绝对路径
report=os.path.join(files,'report')
report_file=os.path.join(report,'report.html')

