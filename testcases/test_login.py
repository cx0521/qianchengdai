#-*-conding:utf-8-*-
#@Time:2019/2/18
#@Author:xiaochen
#@File:登录接口

import unittest
from libext.ddtnew import ddt,data
from common.request import HttpRequest
from common.doexcel import DoExcel
from common.contants import cases_dir
from common.logger import get_logger

logger=get_logger("login")

@ddt
class LoginTest(unittest.TestCase):
    request = HttpRequest()
    doexcel = DoExcel(cases_dir)
    cases = doexcel.read("login")  # 获取登录的测试用例

    def setUp(self):
        pass

    @data(*cases)
    def test_login(self,case):
        logger.info("正在执行{}条用例,用例标题:{}".format(case["case_id"],case["title"]))
        res=self.request.request(case["method"],case["url"],case["data"])
        print("请求的url:",res.url)
        print("响应的结果:",res.json())
        try:
            # 用期望结果和实际结果做断言
            self.assertEqual(case["expectedresult"],res.text,"login error")
            #如果期望结果和实际结果相等，就写回
            self.doexcel.write_back("login",case["case_id"]+1,res.text,"PASS")
            logger.error("第{}条用例执行结果:PASS".format(case["case_id"]))
        except AssertionError as e:
            self.doexcel.write_back("login",case["case_id"]+1,res.text,"Fail")
            logger.error("第{}条用例执行结果:FAIL".format(case["case_id"]))
            raise e

    def tearDown(self):
        pass


if __name__=="__main__":
    unittest.main()

