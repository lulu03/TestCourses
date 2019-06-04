from flask import Flask,request,jsonify     # 导入Flask、request、jsonify类
from d053002_dbtools import query,commit    

app = Flask(__name__)                       # 实例化 Flask app

@app.route("/")     # 没有 methods，默认用 get 接口
def index():
    return "<h1>浪晋的测试小讲堂</h1>"

@app.route("/namelist")
def namelist():
    namelist = {
        1: {"name": "李鑫"},
        2: {"name": "陈倩"},
        3: {"name": "张奕佳"}
    }
    return jsonify(namelist)

@app.route("/reg", methods=["Post"])
def reg():
    reginfo = request.get_json()
    username = reginfo["username"]
    password = reginfo["password"]
    sql = "insert into info (username, password) values ('{}', '{}'); ".format(username, password)
    jieguo = commit(sql)
    res = {}
    res["data"] = reginfo
    res["msg"] = jieguo

    return jsonify(res)



if __name__ == "__main__":
    app.run(debug=True)