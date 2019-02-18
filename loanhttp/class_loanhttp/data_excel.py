# -*- coding:utf-8 -*- 
# @Time    :2019/1/1814:08
# @File    :.py
import os;
#接受表格里的数据的内容
class Data_Excel:
    def __init__(self):
        self.case_id=None;#接受测试用例的编号
        self.title=None;#接受测试用例的标题
        self.url=None;#接收测试用例的http地址
        self.datas=None;#接收测试用例的数据
        self.methed=None;#接收http访问的方式
        self.expectations=None;#接收测试用例的期望值
        self.actual=None;#接收测试用例的实际值
        self.state=None;#接收执行测试用例的状态 是过还是错