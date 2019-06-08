from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class PySelenium():

    def __init__(self, brower="chrome", url=None, exe_path="G:\\TestCourses\\unittest_hw0604\\driver\\chromedriver.exe"):
        brower = brower.lower()

        if brower == "chrome" or brower == "ch":
            self._driver = webdriver.Chrome(executable_path=exe_path)
        if brower == "firefox" or brower == "ff":
            self._driver = webdriver.Firefox(executable_path=exe_path)
        if brower == "internet explorer" or brower == "ie":
            self._driver = webdriver.Ie(executable_path=exe_path)
        if brower == "edge" or brower == "ed":
            self._driver = webdriver.Edge(executable_path=exe_path)

        try:
            self._driver.get(url)
        except:
            print("浏览器打开失败！")

    def get_origin_driver(self):
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
            print("输入的格式必须是(by, value)格式")

        try:
            element = WebDriverWait(self._driver, 30).until(lambda s: s.find_element(*locator))
            return element
        except:
            raise Exception("未找到元素{}！".format(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def type(self, locator, keywords):
        self.find_element(locator).find_element_by_class_namesend_keys(keywords)

    def move_to_element(self, locator):
        '''
            移动到某个元素上
        '''
        e = self._driver.find_element(locator)
        ActionChains(self._driver).move_to_element(e).perform()

    def doese_exist(self, locator):
        '''
            判断元素是否存在
        '''
        try:
            self.find_element(locator)
            return True
        except:
            return False


if __name__ == "__main__":
    pyselenium = PySelenium(url="http://118.24.29.59:8080/morning/", exe_driver="G:\\TestCourses\\SeleniumTest\\driver\\chromedriver.exe")
