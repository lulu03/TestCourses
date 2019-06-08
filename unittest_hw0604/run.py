'''
新建一个run.py入口
'''

import unittest
from utils.HTMLTestRunner import HTMLTestRunner


# 1. 去查找testcase模块下面的所有的testcase开头的 .py 文件结束的py文件
# ./testcase：run.py所对应的相对路径
#  testcase*.py：所有满足这个一个表达式的 py 文件
testcases = unittest.defaultTestLoader.discover("./testcases", "testcase*.py")

# 2. 把所有测试用例装载到测试集里面
testsuites = unittest.TestSuite()
testcases.addTest(testcases)
print(testcases.__dict__)

# 3. 去运行测试集
# 第一种：使用unittest自带的TextTestRunner去运行测试集
# runner = unittest.TextTestResult()
# runner.run(testsuites)

# 第二种：使用HTMLTestRunner这个工具去运行测试集，并生成高大上的html网页版的测试报告
title = "测试报告"
descr = "这是猫宁商城的测试报告"
file_path = "./reports/unittest_report.html"
# 新建一个html文件，把文件的对象赋值为f；wb：如果存在就替换，如果不存在就创建
with open(file_path, "wb") as f:    # 作用等同于后面两句代码：① f = open(file_path, "wb")  ② f.close()
    # 把测试结果放到这个html里面，就是去填写测试报告的内容
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    # 运行测试集
    runner.run(testsuites)
