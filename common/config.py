#-*-conding:utf-8-*-
#@Time:2019/2/20
#@Author:xiaochen
#@File:配置文件类

import configparser
from common import contants

class Readconfig:
    """读取配置文件的类"""
    def __init__(self):
        self.config=configparser.ConfigParser() #调用configparser模块下来的ConfigParser(）实例化一个对象config
        self.config.read(contants.global_dir) #加载总开关的配置文件路径
        open=self.config.getboolean("switch","open") #获取文件里面的值，总开关的配置文件设置的是布尔值，所以用getboolean获取；字符串就是get获取

        #方便环境的切换
        if open:
            self.config.read(contants.test_dir)#如果总开关配置文件设置的是True，就加载test_dir路径
        else:
            self.config.read(contants.test2_dir)#如果总开关配置文件设置的是False，就加载test2_dir路径

    def get_readconfig(self,section,option): #获取字符串
        # Readconfig类把config.get()封装了，所以要给类本身封装一个方法，用处和config.get()一样，直接Readconfig().get()就可以调用get方法来获取数据了
        return self.config.get(section,option)

        #如果不封装get方法，要获取config里面的get方法，就要
        # read_config=Readconfig()
        # read_config.config.get() #自己定义的Readconfig没有get的方法

    def getboolean_readconfig(self,section,option):#获取布尔值
        #意义同上
        return self.config.getboolean(section,option)


if __name__=="__main__":
    read_config=Readconfig()
    result=read_config.get_readconfig("api","pre_url")
    print(result)