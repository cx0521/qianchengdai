#-*-conding:utf-8-*-
#@Time:2019/2/23
#@Author:xiaochen
#@File:把日志写成一个函数，方便后面模块的调用

# 输出控制台，定义输出级别debug
# 输出到文件，文件路径请使用绝对路径 logs
# 根据读取配置文件的option来确认输出到控制台和文件的日志级别

import logging
import logging.handlers #调用logging.handlers里面的RotatingFileHandler方法，进行日志的限制最大字节数，优化系统
import os
from common import contants
from common.config import Readconfig

config=Readconfig()#实例化一个config对象，用config对象调用里面的方法

def get_logger(logger_name):
    #1.调用logging模块中getLogger方法，创建一个收集器:logger
    logger=logging.getLogger(logger_name)#必须要传一个收集器的名字进去，否则默认取root的收取日志的级别
    #设置收集器收集日志的级别，最好是最低日志的级别
    logger.setLevel("DEBUG")

    #2.设置日志输出的格式
    log_format=logging.Formatter("%(asctime)s-""%(levelname)s-""%(filename)s-""%(name)s-""%(lineno)d""[日志信息]:%(message)s")

    #3.创建输出渠道(控制台和文件)

    #输出到控制台：根据配置文件中设置日志级别
    console_level=config.get_readconfig("log","console_handler")

    console_handler=logging._StderrHandler()
    console_handler.setLevel(console_level)#console_level是从配置文件中获取出来的值

    #输出到文件：根据配置文件中设置日志级别
    file_level=config.get_readconfig("log","file_handler")
    file_name=os.path.join(contants.logs_dir,"xiaochen.logs")#使用绝对路径，把生成的日志放到logs文件夹下

    file_handler=logging.handlers.RotatingFileHandler(file_name,maxBytes=20*1024*1024, backupCount=10, encoding="utf-8")
    file_handler.setLevel(file_level)#file_level是从配置文件中获取出来的值

    #4.对接：收集器与渠道的对接
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    #设置渠道的文件格式
    console_handler.setFormatter(log_format)
    file_handler.setFormatter(log_format)

    return logger #要把对象返回去，要不自定义的函数get_logger就没有logging和logger的方法了

if __name__=="__main__":
    logs=get_logger("xiaochen")

    logs.debug("this is debug!")
    logs.info("this is info!!")
    logs.warning("this is warning!!!")
    logs.error("this is error!!!!")
    logs.critical("this is critical!!!!!")

    # get_logger("xiaochen").critical("this is critical!!!!!") #mongo老师，为什么我这样调用，就会显示2条日志呢？