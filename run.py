#-*-conding:utf-8-*-
#@Time:2019/2/23
#@Author:xiaochen
#@File:统一运行测试方法

#使用unittest.defaultTestLoader.discover()自动查找testcases文件夹下，以test_开头的.py文件里面的测试类
import unittest
from common import contants
import HTMLTestRunnerNew

all_test=unittest.defaultTestLoader.discover(contants.testcases_dir, pattern='test_*.py',top_level_dir=None)

#利用上下文管理器自动关闭资源
with open(contants.reports_html,"wb+") as file:    #选择绝对路径，把文件打开，写进内容

    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            title="前程贷测试报告",
                                            description="2019.2.23测试报告",
                                            tester="xiaochen")

    runner.run(all_test)
