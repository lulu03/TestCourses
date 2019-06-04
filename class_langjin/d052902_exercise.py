from selenium import webdriver
import time
# 对浏览器进行实例化
driver = webdriver.Chrome(executable_path="..\chromedriver.exe")
# 打开浏览器
driver.get("http://http://118.24.29.59:8080")
time.sleep(5)

# 用户信息
phone = "13450411910"
password = "123456"


# 注册
driver.find_element_by_id("J_header_lnkRegister").click()
time.sleep(5)
driver.find_element_by_id('username').send_keys(phone)
driver.find_element_by_id('getCode').click()
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('rePassword').send_keys(password)
time.sleep(5)
driver.find_element_by_id('btnReg').click()


# 登录
driver.find_element_by_id('username').send_keys(phone)
driver.find_element_by_id('password').send_keys(password)
time.sleep(5)
driver.find_element_by_id('btnLogin').click()

# 判断是否登录成功
txt = driver.find_element_by_id('').text
if phone in txt:
    print("登录成功！测试成功！")
else:
    print("登录失败！测试失败！")

# 关闭浏览器
driver.quit()