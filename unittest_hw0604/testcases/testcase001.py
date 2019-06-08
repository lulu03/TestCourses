from utils.PySelenium import PySelenium
import unittest
import time


class TestCase(unittest.TestCase):

    def setUp(self):
        self._pydriver = PySelenium(url="http://118.24.29.59:8080/morning/")
        self.driver = self._pydriver.get_origin_driver()
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(5)
        self._pydriver.quit()

    def test_01_login(self):
        '''
            登录的测试用例
        '''
        # 点击
        login = ("link text", "登录")
        self._pydriver.click(login)

        # 登录操作
        username = ("id", "adminNo")
        password = ("id", "password")
        login_btn = ("id", "btn_login")
        self._pydriver.type(username, "13000000000")
        self._pydriver.type(password, "a123456")
        self._pydriver.click(login_btn)

        # 断言
        assert_text = ("link text", "配件")
        self.assertTrue(self._pydriver.doese_exist(assert_text))

    def test_02_shopping(self):
        '''
            加入购物车测试用例
        '''
        # 搜索
        search = ("id", "searchInput")
        search_btn = ("css selector", "#zySearch > button")
        self._pydriver.type(search, "智能摄像机")
        self._pydriver.click(search_btn)

        # 跳转到购物车页面
        shexiangji = ("xpath", '//*[@id="products-list"]/ul/li/div[2]/div[1]/p/a')
        self._pydriver.move_to_element(shexiangji)
        self._pydriver.click(shexiangji)
        # goods = ("xpath", '//*[@id="products-list"]/ul/li/div[1]/a/img')

        # 加入购物车页面去点击加入购物车
        self.driver.switch_to_window(self.driver.window_headles[-1])
        add = ("class name", "cart")
        self._pydriver.click(add)
        # add = ("text link", "加入购物车")
        # self._pydriver.click(add)
        # buy = ("id", "buy")
        # self._pydriver.click(buy)

        # 断言成功操作
        message = ("id", "message")
        self.assertTrue(self._pydriver.doese_exist(message))

# unittest.main()
