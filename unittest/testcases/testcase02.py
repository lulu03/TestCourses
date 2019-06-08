import unittest
from selenium import webdriver

import time

class TestCaseLogin(unittest.TestCase):

    @classmethod    # 表示这是一个类方法
    def setUpClass(cls):
        print("这是setUpClass方法")
    
    @classmethod
    def tearDownClass(cls):
        print("这是tearDownClass方法")

    def setUp(self):
        """
            每个方法执行之前都来执行这个方法，初始化操作
        """
        # self.driver 实际上就变成了成员变量，这个变量就能够在不同的成员方法里面来运行了
        self.driver = driver = webdriver.Chrome(executable_path="G:\TestCourses\chromedriver.exe")
        self.driver.get("http://localhost:8080/")
  
    def tearDown(self):
        '''
            每个方法执行之后，都来执行这个方法，关掉浏览器的操作
        '''
        self.driver.close()

    def test_01_login(self):
        self.driver.find_element_by_id("J_header_InkLogin").click()
        self.driver.find_element_by_id("username").send_keys("13000000000")
        self.driver.find_element_by_id("password").send_keys("a123456")
        self.driver.find_element_by_id("btnLogin").click()

    def test_02_register(self):
        # self.driver.maximize_window()        # 把浏览器最大化
        self.driver.find_element_by_id("J_header_InkRegister").click()
        self.driver.find_element_by_id("username").send_keys("13900000001")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("rePassword").send_keys("123456")
        self.driver.find_element_by_id("getCode").click()
        



# unittest.main()
