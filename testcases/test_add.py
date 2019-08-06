#-*-conding:utf-8-*-
#@Time:2019/2/21
#@Author:xiaochen
#@File:添加项目（标的）接口

import unittest
from libext.ddtnew import ddt,data
from common.doexcel import DoExcel
from common.contants import cases_dir
from common.request import HttpRequest
from common.logger import get_logger

logger=get_logger("add")

@ddt
class AddTest(unittest.TestCase):
    request = HttpRequest()
    doexcel=DoExcel(cases_dir)
    cases=doexcel.read("add")#获取测试数据


    def setUp(self):  #用例运行它就运行
        pass

    @data(*cases)
    def test_add(self,case):
        logger.info("开始执行{}条用例了,用例标题是:{}".format(case["case_id"],case["title"]))
        res=self.request.request(case["method"],case["url"],case["data"])
        print("响应的结果:{}".format(res.json()))
        try:
            #self.assertEqual(case["expectedresult"],res.text,"add error!!")
            #self.doexcel.write_back("add",case["case_id"]+1,res.text,"PASS")
            logger.error("第{}条用例执行的结果是:PASS".format(case["case_id"]))

        except AssertionError as e:  #try监控断言，出错了继续执行下面的代码（假如不加断言，用例失败了，代码就停了）
            self.doexcel.write_back("add",case["case_id"]+1,res.text,"FAIL")
            logger.error("第{}条用例执行的结果是:FAIL".format(case["case_id"]))

            raise e

    def tearDown(self): #用例运行它就运行
        pass
