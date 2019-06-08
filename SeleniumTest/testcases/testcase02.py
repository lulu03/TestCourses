'''
动态查找元素
'''

# 第一种：强制等待，time（不推荐使用，容易出现问题）
# import time
# time.sleep(3)
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class TestCase02(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="G:\\TestCourses\\SeleniumTest\\driver\\chromedriver.exe")
        self.driver.get("http://118.24.29.59:8080/")
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    @unittest.skip("测试")  # 跳过测试用例执行
    def test_01_login(self):
        # 静态查找
        # e = self.driver.find_element_by_id("J_header_lnkLogin").click()

        # 动态查找
        # 使用find_element 是为了方便以后动态封装
        # 写法一
        # e = WebDriverWait(self.driver, 30).until(lambda s: s.find_element("id", "J_header_lnkLogin"))

        # 写法二：
        login_button = ("id", "J_header_lnkLogin")                                          # 登录的元素定位方式和值
        e = WebDriverWait(self.driver, 30).until(lambda s: s.find_element(*login_button))   # s.find_element(*login_button)=s.find_element()；e就是元素
        e.click()

    @unittest.skip("测试")      # 跳过测试用例执行
    def test_02_mouse(self):
        '''
            鼠标事件：
                - perform():执行所有的ActionChains所定义的行为
                - context_click():右击
                - double_click():双击
                - drag_and_drop():拖动
                - move_to_element():悬停
        '''

        login_link = ("id", "J_header_lnkLogin")
        e = WebDriverWait(self.driver, 30).until(lambda s: s.find_element(*login_link))

        # 首先把鼠标移动上去，才能进行右键
        # ActionChains(self.driver).move_to_element(e).perform()  # 悬停
        # ActionChains(self.driver).context_click(e).perform()    # 右键
        ActionChains(self.driver).double_click(e).perform()     # 双击

    @unittest.skip("测试")
    def test_03_keyboard(self):
        '''
            键盘事件：
                - Keys.BACK_SPACE：删除键
                - Keys.SPACE：空格键
                - Keys.TAB：Tab键
                - Keys.ESCAPE：回退键
                - Keys.ENTER：回车键
                - Keys.CONTROL,”a”：组合键，Ctrl + A
                - Keys.CONTROL,”x”：组合键，Ctrl + X
                - Keys.CONTROL,”v”：组合键，Ctrl + V
                - Keys.CONTROL,”c”：组合键，Ctrl + C
                - Keys.F1：F1键
                - Keys.F12：F12键
        '''

        search_input = ("id", "keyword")
        e = WebDriverWait(self.driver, 30).until(lambda s: s.find_element(*search_input))
        e.send_keys("葡萄萄")
        time.sleep(3)
        e.send_keys(Keys.BACK_SPACE)

        e.send_keys(Keys.ENTER)

    def test_04_iframe(self):
        '''
            selenium 作用域
        '''
        self.driver.get("http://passport2.eastmoney.com/pub/login")

        # 1. 切换到子网页的作用域
        # 找到这个iframe元素，并且切换过去
        iframe = ("id", "frame_login")
        e = WebDriverWait(self.driver, 3).until(lambda s: s.find_element(*iframe))    # 首先找到iframe
        self.driver.switch_to_frame(e)                                                  # 切换到iframe

        username = ("id", "txt_account")
        e = WebDriverWait(self.driver, 3).until(lambda s: s.find_element(*username))
        e.send_keys("13000000001")

        # 如果需要找父元素了，就要切换到默认的作用域，大网页
        self.driver.switch_to_default_content()

        # 2. 找大网页的元素
        add = ("link text", "关于我们")
        e = WebDriverWait(self.driver, 3).until(lambda s: s.find_element(*add))
        e.click()


unittest.main()
