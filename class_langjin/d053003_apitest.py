import requests
from d053002_dbtools import query

url = "http://127.0.0.1:5000/reg"
headers = {"Content-Type": "application/json"}
data = {"username": "xiaobai", "password": "123456"}
res = requests.post(url, headers=headers, json=data)
res = res.json()    # 把res从文本格式变成 json 格式
# print(res)
sql = "select * from info where username = '{}';".format(data['username'])
dbres = query(sql)
print(dbres)
if res["msg"] == True:
    if dbres[0][1] == data["username"]:
        print("测试通过，注册成功！")
    else:
        print("测试失败，数据没有正常的写入数据库")
else:
    print("测试失败！")
print(res)