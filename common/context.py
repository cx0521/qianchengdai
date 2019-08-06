#-*-conding:utf-8-*-
#@Time:2019/2/22
#@Author:xiaochen
#@File:

# s 是目标字符串
# d 是替换的内容
# 找到目标字符串里面的标识符KEY，去d里面拿到替换的值
# 替换到s 里面去，然后再返回
import re

def replace(s,d):
    p="\$\{(.*?)}"   #正则表达式
    while re.search(p,s):
        m=re.search(p,s)  #在s中找到有这个表达式的标识，把字典里面的替换进去
        key=m.group(1)        #只找到第一组
        value=d[key]
        s=re.sub(p,value,s,count=1)

    return s

s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
d = {"admin_user": "13707791215", "admin_pwd": "123456"}
r=replace(s,d)
print(r)