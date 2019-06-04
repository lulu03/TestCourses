# 异常处理
# 如果 try 不报错，执行 try，如果 try 报错，执行 except


# try:
#     print(1/0)
# except:
#     print("哈哈哈")


# try:
#     print(1/2)
# except:
#     print("嘻嘻嘻")



import requests

url = "http://118.24.29.59:5000//userRegister"
headers = {'Content-Type': "application/json"}
data = {"username":"test","password":"test","nickname":"123456"}
res = requests.post(url, headers=headers, json=data)
try:
    res = res.json()
    if res["msg"] == "用户名已存在！":
        print("测试通过！")
    else:
        print("测试失败！")
except:
    print("接口异常，没有正常返回数据")
