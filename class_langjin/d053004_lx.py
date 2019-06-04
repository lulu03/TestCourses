import requests
from d053002_dbtools import query

url = "http://127.0.0.1:5000/reg"
headers = {'Content-Type': "application/json"}
payload = {"username": "lisi", "password": "123456"}
response = requests.request("POST", url, json=payload, headers=headers)
res = response.json()
print(res)
sql = "select * from info where username = '{}';".format(payload["username"])
jieguo = query(sql)
print(jieguo)
if res["msg"] == True:
    if jieguo[0][1] == payload["username"]:
        print("测试通过！注册成功！")
    else:
        print("测试失败！数据没有正常写入数据库！")
else:
    print("测试失败！")