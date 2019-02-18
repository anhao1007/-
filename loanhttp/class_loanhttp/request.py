# -*- coding:utf-8 -*- 
# @Time    :2019/1/199:54
# @File    :.py
import requests
from conf.conf_read import Config;
from class_loanhttp import files_os
class Methed:
    def __init__(self):
        self.session=requests.sessions.session()#实例化一个session
    def request(self,method,url,data=None):
        method=method.upper()#将字符转成全部大写
        if data is not None and type(data)==str:
         # 字符串转字典
         data=eval(data)
        #url的拼接
        conf = Config(files_os.conf_file)#实例化配置文件的类
        conf_url = conf.read_conf()#调用配置文件中的读取方法
        url = conf_url + url;#URL进行拼接
        if method=='GET':
            return  self.session.request(method,url=url,params=data)
        elif method=='POST':
            return  self.session.request(method,url=url,data=data)
        else:
            print("Un-support method!!!")

