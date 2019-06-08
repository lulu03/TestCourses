# 1. 导入unittest
import unittest

# 2. 去继承unittest.TestCase
class TestCase01(unittest.TestCase):

    def test_01_demo1(self):
        print("这是TestCase01的第一个测试用例")
    
    def test_02_demo2(self):
        print("这是TestCase01的test_02_demo2")

# test = TestCase01()
# test.test_01_demo1()

# 运行方法
# unittest.main()