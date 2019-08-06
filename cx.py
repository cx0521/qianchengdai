#-*-conding:utf-8-*-
#@Time:2019/7/13
#@Author:xiaochen
#@File:

import requests

class HttpRequests:
    '''把get和post封装成为一个类'''
    def __init__(self):
        self.session = requests.sessions.Session() #创建一个session会话，保存账号是登录状态

    def request(self,method,url,data=None):  #data给None，因为get是通过params传参，post是通过data传参
        if method.upper()=='GET':
            res = self.session.request(method,url,params=data)
        elif method.upper()=='POST':
            res = self.session.request(method,url,data=data)
        else:
            print('Un-support method !!!')

        return res

    def close_session(self):
        self.session.close()


if __name__=="__main__":

    seseion = HttpRequests()
    res1 = seseion.request('post','http://test.lemonban.com/futureloan/mvc/api/member/login',{'mobilephone':'13707790001','pwd':'123456'})
    print(res1.text)
    res2 = seseion.request('post','http://test.lemonban.com/futureloan/mvc/api/member/recharge',{'mobilephone':'13707790000','amount':'10'})
    print(res2.text)