#-*-conding:utf-8-*-
#@Time:2019/1/21
#@Author:xiaochen
#@File:常量

#读取测试数据，要使用绝对路径，不能用相对路径。（封装一个绝对路径的类）

import os

#1.获取项目的根路径
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
base_dir=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

#2.把项目的根路径和测试数据的根目录拼接起来
datas_dir=os.path.join(base_dir,"datas")
print(datas_dir)
#测试用例的路径
cases_dir=os.path.join(datas_dir,"cases.xlsx")

#3.配置文件的目录
conf_dir=os.path.join(base_dir,"conf")

#global.conf文件路径
global_dir=os.path.join(conf_dir,"global.conf")
#test.conf文件路径
test_dir=os.path.join(conf_dir,"test.conf")
#test2.conf文件路径
test2_dir=os.path.join(conf_dir,"test2.conf")

#logs日志文件夹的路径
logs_dir=os.path.join(base_dir,"logs")

#测试类文件夹的路径
testcases_dir=os.path.join(base_dir,"testcases")

#测试报告文件夹的路径
reports_dir=os.path.join(base_dir,"reports")

#测试报告文件的路径
reports_html=os.path.join(reports_dir,"qianchendai-API.html")




if __name__=="__main__":

    print("测试用例的路径:",cases_dir)
    print("配置文件总开关的路径:",global_dir)
    print("配置文件test的路径:",test_dir)
    print("配置文件test2的路径:",test2_dir)