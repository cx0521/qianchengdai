#-*-conding:utf-8-*-
#@Time:2019/1/18
#@Author:xiaochen
#@File:httprequest.py

import requests
from common.config import Readconfig

class HttpRequest:
    """这是一个具有GET和POST请求的类"""

    def __init__(self):
        self.session=requests.sessions.session() #建立一个session会话，保存cookies

    def request(self,method,url,data=None):#data指的是excel表中的测试数据

        config = Readconfig() #自定义配置文件的封装类，实例化一个对象
        pre_url=config.get_readconfig("api","pre_url") #获取的是配置文件里面的pre_url
        url=pre_url+url#配置文件里pre_url和excel表中url的拼接

        if data is not None and type(data)==str: #如果excel表中的数据不为空，或者是字符串类型，就使用eval（）
            data=eval(data)#因为excel表中的数据类型是字符串，data要传字典，所以可以用eval()函数，保存自身数据类型

        if method.upper()=="POST":
            res=self.session.request(method,url=url,data=data)
            return res
        elif method.upper()=="GET":
           res=self.session.request(method,url=url,params=data)
           return res
        else:
            print("Un-support method !!!")

    #关闭session
    def close(self):
        self.session.close()


