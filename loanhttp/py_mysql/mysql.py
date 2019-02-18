# -*- coding:utf-8 -*- 
# @Time    :2019/1/2210:14
# @File    :.py
import pymysql
class Mysql_operation:
    def __init__(self):
        host='test.lemonban.com';
        user='test'
        passwd='test'
        port=3306
        self.mysql=pymysql.connect(host=host,user=user,password=passwd,database='future',port=port);#创建连接
        self.cursor=self.mysql.cursor()#建立查询
    def query(self,sql):
        self.cursor.execute(sql)#执行sql
        result=self.cursor.fetchall()#获取结果
        return  result
    def close(self):
        self.cursor.close();#关闭查询
        self.mysql.close();#关闭数据库