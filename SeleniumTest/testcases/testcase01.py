# 1. 导入unittest
import time
import unittest
from selenium import webdriver


# 2. 去继承unittest.TestCase
class TestCase01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="G:\TestCourses\SeleniumTest\driver\chromedriver.exe")
        self.driver.get("http://118.24.29.59:8080/morning/user/userLogin")
    
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_01_demo1(self):

        # id：能用id就用id
        self.driver.find_element_by_id("adminNo").send_keys("12345")

        # xpath
        # self.driver.find_element_by_xpath('//*[@id="adminNo"]').send_keys("12345")

        # name
        # self.driver.find_element_by_name('user.loginName').send_keys("12345")

        # class
        # self.driver.find_elements_by_class_name("txt03 f-r3 required").send_keys("12345")

        # tag
        # e = self.driver.find_element_by_tag_name("")
        # print(e.text)

        # css selector
        # self.driver.find_elements_by_css_selector("#adminNo").send_keys("12345")

        # link text
        # self.driver.find_elements_by_link_text("猫宁商城").click()

        # partial link text
        # self.driver.find_elements_by_partial_link_text("猫宁").click()


if __name__ == "__main__":
    unittest.main()