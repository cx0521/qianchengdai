#-*-conding:utf-8-*-
#@Time:2019/2/18
#@Author:xiaochen
#@File:注册接口

import unittest
from libext.ddtnew import ddt,data
from common.request import HttpRequest
from common.doexcel import DoExcel
from common.contants import cases_dir
from common.mysql import MysqlUtil
from common.logger import get_logger

logger=get_logger("register")

@ddt
class RegisterTest(unittest.TestCase):
    request = HttpRequest()
    doexcel=DoExcel(cases_dir)
    cases=doexcel.read("register")#获取注册的测试用例


    # print(type(max_mobilephone))#数据库取出来的vachar类型，也就是str类型

    def setUp(self):  #每个用例执行开始前，都要运行，获取数据库里面最大的手机号
        self.mysql = MysqlUtil()  # 创建数据库连接，打开查询页面
        sql = "select MAX(MobilePhone)from future.member"  # 查询数据库里面最大的手机号
        self.max_mobilephone = self.mysql.fetch_one(sql)[0]  # 从数据库里面查询出来的数据类型是：元组，要用下标取值;数据库里面最大的手机号是：max_mobilephone

    @data(*cases)
    def test_register(self,case):
        logger.info("正在执行{}条用例,用例标题是:{}".format(case["case_id"],case["title"]))

        import json
        data_dict=json.loads(case["data"])#excel表中的data数据是str类型，需要转成json字典格式的字符串

        if data_dict["mobilephone"]=="$register_mobilephone":#转成json格式，可以根据key取值，判断value是否等于excel表中做的标记$register_mobilephone
            data_dict["mobilephone"]=int(self.max_mobilephone)+1  #如果value等于excel表中做的标记$register_mobilephone，那查出来的最大手机号再加上1，再去请求

        # 调用请求接口，接口请求后，会有返回结果，也就是实际结果
        res=self.request.request(case["method"],case["url"],data_dict) #把case[data]换成最新的data_dict字典去做请求

        #预期结果和实际结果的断言
        try:
            self.assertEqual(case["expectedresult"],res.text,"register error!!!")
            #断言成功，测试结果就写PASS
            self.doexcel.write_back("register",case["case_id"]+1,res.text,"PASS")
            logger.error("第{}条用例执行的结果是:PASS".format(case["case_id"]))
        except AssertionError as e:
            # 断言失败，测试结果就写Fail
            self.doexcel.write_back("register",case["case_id"]+1,res.text,"FAIL")
            logger.error("第{}条用例执行的结果是:FAIL".format(case["case_id"]))
            raise e

    def tearDown(self):
        self.mysql.close()
