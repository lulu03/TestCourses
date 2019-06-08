'''
    selenium的二次封装
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class PySelenium():

    def __init__(self, browser="chrome", url=None, exe_driver="G:\\TestCourses\\SeleniumTest\\driver\\chromedriver.exe"):
        '''
            初始化SeleniumDriver并且打开浏览器
        '''

        browser = browser.lower()   # 把浏览器参数所有的大写字母转成小写，方便我们操作

        # 1. 判断打开的浏览器类型，并且打开浏览器
        if browser == "chrome" or browser == "ch":
            self._driver = webdriver.Chrome(executable_path=exe_driver)
        if browser == "firefox" or browser == "ff":
            self._driver = webdriver.firefox(executable_path=exe_driver)
        if browser == "internet explorer" or browser == "ie":
            self._driver = webdriver.Ie(executable_path=exe_driver)
        if browser == "edge" or browser == "ed":
            self._driver = webdriver.Edge(executable_path=exe_driver)

        try:
            self._driver.get(url)
        except:
            print("浏览器打开失败")

    def get_origin_driver(self):
        '''
            获取webdriver的初始化浏览器对象
        '''
        return self._driver

    def find_element(self, locator):
        '''
            查到单个元素
                参数：locator=("id", "123")
                类型：
                ID = "id"
                XPATH = "xpath"
                LINK_TEXT = "link text"
                PARTIAL_LINK_TEXT = "partial link text"
                NAME = "name"
                TAG_NAME = "tag name"
                CLASS_NAME = "class name"
                CSS_SELECTOR = "css selector"
        '''
        if not isinstance(locator, tuple):
            raise Exception("输入的格式必须是(by, value)格式！")

        try:
            element = WebDriverWait(self._driver, 30).until(lambda s: s.find_element(*locator))
            return element
        except:
            raise Exception("未找到元素{}！".format(locator))

    def click(self, locator):
        '''
            查找元素并点击元素
        '''
        self.find_element(locator).click()

    def type(self, locator, keywords):
        '''
            查找元素并输入文本
        '''
        self.find_element(locator).send_keys(keywords)


if __name__ == "__main__":
    pyselenium = PySelenium(url="http://118.24.29.59:8080/", exe_driver="G:\\TestCourses\\SeleniumTest\\driver\\chromedriver.exe")

    login = ("id", "J_header_lnkLogin")
    username = ("id", "username")
    # pyselenium.find_element(login)
    pyselenium.click(login)
    pyselenium.type(username, "13000000001")
