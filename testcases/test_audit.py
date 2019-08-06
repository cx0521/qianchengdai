#-*-conding:utf-8-*-
#@Time:2019/2/21
#@Author:xiaochen
#@File:审核接口

import unittest
from libext.ddtnew import ddt,data
from common.doexcel import DoExcel
from common import contants
from common.request import HttpRequest
from common.logger import get_logger

logger=get_logger("audit")

@ddt
class AuditTest(unittest.TestCase):
    doexcel=DoExcel(contants.cases_dir)
    cases=doexcel.read("audit")
    request=HttpRequest()

    def setUp(self):
        pass

    @data(*cases)
    def test_audit(self,case):
        logger.info("执行第{}条用例,用例标题是:{}".format(case["case_id"],case["title"]))

        res=self.request.request(case["method"],case["url"],case["data"])
        print("响应的结果:{}".format(res.json()))

        try:
            self.assertEqual(case["expectedresult"],res.text,"audit error")
            self.doexcel.write_back("audit",case["case_id"]+1,res.text,"Pass")
            logger.error("第{}条用例执行的结果是:PASS".format(case["case_id"]))

        except AssertionError as e:
            self.doexcel.write_back("audit",case["case_id"]+1,res.text,"Fail")
            logger.error("第{}条用例执行的结果是:FAIL".format(case["case_id"]))

            raise e

    def tearDown(self):
        pass
