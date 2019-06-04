import pymysql

# 连接数据库
# 选择数据库
# 执行sql命令

def query(sql):
    '''
    数据库的查询功能，请传入SQL语句
    '''
    dbinfo = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "123456",
        "db": "ceshi"
    }
    # 连接数据库
    db = pymysql.connect(**dbinfo)
    # 获取游标
    cursor = db.cursor()
    # 执行SQL
    cursor.execute(sql)
    # 获取返回值
    res = cursor.fetchall()
    return res


def commit(sql):
    '''
    数据库的增加/修改/删除功能
    '''
    dbinfo = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "123456",
        "db": "ceshi"
    }
    # 连接数据库
    db = pymysql.connect(**dbinfo)
    # 获取游标
    cursor = db.cursor()
    try:
        # 执行SQL
        cursor.execute(sql)
        # 提交应用
        db.commit()
        return True
    except:
        return False

# sql = "insert into f_info(id, info) values (4, '陈倩');"
# res =commit(sql)
# print(res)