from selenium import webdriver      # 导入包
import time                         # 导入时间包
# 对浏览器进行实例化
driver = webdriver.Chrome(executable_path="../chromedriver.exe")     # 定义对象
time.sleep(5)
# 打开登录的网址
driver.get("http://118.24.29.59:8080/")
time.sleep(5)
# 注册
driver.find_element_by_id("J_header_lnkRegister").click()   # find_element_by_：定位
time.sleep(5)
phone = "13450411944"
driver.find_element_by_id("username").send_keys(phone)
driver.find_element_by_id("getCode").click()
password = "a123456"
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("rePassword").send_keys(password)
time.sleep(5)
driver.find_element_by_id("btnReg").click()
time.sleep(5)

# 登录
driver.find_element_by_id("username").send_keys(phone)
driver.find_element_by_id("password").send_keys(password)
time.sleep(5)
driver.find_element_by_id("btnLogin").click()
time.sleep(10)

# 判断是否登录成功
txt = driver.find_element_by_id("J_head_log").text      # 获取元素里的文本信息
# print(txt)
if phone in txt:
    print("登录成功！测试通过！")
else:
    print("登录异常！测试失败！")


# 关闭浏览器
driver.quit()
