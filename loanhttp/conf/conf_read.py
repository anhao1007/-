# -*- coding:utf-8 -*- 
# @Time    :2019/1/2114:41
# @File    :.py
from configparser import ConfigParser;
from class_loanhttp import files_os
class Config:
    #初始化类的对象
    def __init__(self,files):
        self.files=files;
    #读取测试用例的内容
    def read_conf(self):
        #实例化配置类
        cf=ConfigParser()
        #打开配置文件
        cf.read(self.files,encoding='utf-8')
        # value=eval(cf.get('Test','test')) #读取值的本来的类型
        value = cf.get('TestURL', 'url')
        return value;
if __name__=='__main__':
    conf=Config(files_os.conf_file)
    confs=conf.read_conf()
    print(confs)