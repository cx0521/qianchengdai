#-*-conding:utf-8-*-
#@Time:2019/2/18
#@Author:xiaochen
#@File:充值接口
import unittest
from libext.ddtnew import ddt,data
from common.doexcel import DoExcel
from common.contants import cases_dir
from common.request import HttpRequest
from common.logger import get_logger
from common.mysql import MysqlUtil

logger=get_logger("recharge")
setattr()

@ddt
class RechargeTest(unittest.TestCase):
    doexcel=DoExcel(cases_dir)
    cases=doexcel.read("recharge")
    request=HttpRequest()#实例化一个对象request，再用request调用里面的函数

    def setUp(self):
        pass

    @data(*cases)
    def test_recharge(self,case):
        logger.info("正在执行{}条用例，用例标题是:{}".format(case["case_id"],case["title"]))
        res=self.request.request(case["method"],case["url"],case["data"])
        print('响应结果:',res.text)

        try:
            self.assertEqual(str(case["expectedresult"]),res.json()["code"],"recharge error!!!")

            self.doexcel.write_back("recharge",case["case_id"]+1,res.text,"PASS")
            logger.error("第{}条用例执行的结果是:PASS".format(case["case_id"]))
        except AssertionError as e:
            self.doexcel.write_back("recharge", case["case_id"] + 1, res.text, "FAIL")
            logger.error("第{}条用例执行的结果是:FAIL".format(case["case_id"]))
            raise e

    def tearDown(self):
        pass