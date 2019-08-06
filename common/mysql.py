#-*-conding:utf-8-*-
#@Time:2019/2/19
#@Author:xiaochen
#@File:封装操作数据库的类
import pymysql

class MysqlUtil:
    """这是一个操作数据库的封装类"""

    #这里需要优化，要放到配置文件里面
    def __init__(self):#把数据库连接，查询页面放在初始化函数，每次事例化对象一次，就自动连接数据库，新建查询
        host="47.107.168.87"
        user="python"
        password="python666"
        # 连接数据库
        self.mysql=pymysql.connect(host=host,user=user,password=password,port=3306)
        # 新建查询光标
        self.cursor=self.mysql.cursor()

    def fetch_one(self,sql):
        """输入sql语句和查询结果函数"""

        #执行sql
        self.cursor.execute(sql)
        #查询结果
        result=self.cursor.fetchone()
        return result

    def close(self):
        """关闭查询和数据库函数"""
        self.cursor.close()
        self.mysql.close()


if __name__=="__main__":
    mysql=MysqlUtil()
    result=mysql.fetch_one("SELECT f.`LeaveAmount`FROM Future.`member` AS f WHERE MobilePhone='13707790001'")[0]
    print(result)
    mysql.close()

