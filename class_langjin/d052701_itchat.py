'''
# 代码一：给单个好友发消息
import itchat                       # 导入微信的包

# 微信自动登录，会生成“itchat.pkl”的文件（加密的，存储的是登录信息）
# 在auto_login()里面提供一个True，即可保留登录状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(hotReload=True)   
friends = itchat.get_friends()      # 获取好友信息
# print(friends)                    # 打印全部好友信息
for i in friends:                   # 遍历好友明细
    print(i)                        # 分开单个好友打印（一个好友信息为一段）
    # 查找单个好友信息并打印出来
    if i["RemarkName"] == "张奕佳":
        UserName == i["UserName"]
        itchat.send_msg("你好啊！", toUserName=UserName)    # msg() 前面写发送的内容，后面写发给谁
        itchat.send_image(fileDir="./桌面图片.jpg", toUserName=UserName)



# 代码二：微信群发消息
import itchat                       # 导入微信的包

# 微信自动登录，会生成“itchat.pkl”的文件（加密的，存储的是登录信息）
# 在auto_login()里面提供一个True，即可保留登录状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(hotReload=True)
friends = itchat.get_friends()      # 获取好友信息
for i in friends:                   # 遍历好友明细
    UserName = i["UserName"]
    itchat.send_msg("你好啊！", toUserName=UserName)    # msg() 前面写发送的内容，后面写发给谁
'''


# 代码三：用postman发送消息给图灵机器人，打印机器人回复的内容
import requests                     # 导入request包

# 给接口发消息
url = "http://open.turingapi.com/v1/openapi"
payload = {"input_text":"你好啊！","user_info":{"open_id":"6a61bda8-07e1-4ae3-ae57-8b1e8cf4f141"},"robot_id":"205535"}
headers = {
    'Content-Type': "application/json"
    }
response = requests.request("POST", url, json=payload, headers=headers)
# print(response.text)              # 打印机器人返回的接口信息
res = response.json()               # 调取机器人返回的接口信息的json（字典格式），赋值
datas = res["result"]["datas"]      # 获取接口信息里，机器人具体回复的内容（在result字典里的datas字典的value键）
# 调用机器人回复的消息在微信回复
for i in datas:                     # 遍历机器人具体回复的内容
    print(i["value"])               # 打印机器人每个回复的内容




# 代码四：微信好友通过我（的微信），跟机器人对话
import itchat                               # 导入微信的包
from itchat.content import *                # 导入全部消息类型
import requests                             # 导入request包

# @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
# 处理文本类消息，包括文本TEXT、位置MAP、名片CARD、通知NOTE、分享SHARING
@itchat.msg_register(TEXT)
# 微信里，每个用户和群聊，都使用很长的ID来区分
# msg['FromUserName']就是发送者的ID
# 将消息的类型和文本内容返回给发送者
def remsg(msg):                             # 只要有人发文本消息，就会自动执行这个方法
    # print(msg)                            # 查看msg内容（好友发来信息所返回的接口信息）
    # print(msg["User"])                    # 查看msg["User"]的内容
    print(msg["User"]["NickName"], "说:", msg["Text"])                      # 打印好友发来的具体内容
    # 给接口发消息
    url = "http://open.turingapi.com/v1/openapi"
    payload = {"input_text": msg["Text"],"user_info":{"open_id":"6a61bda8-07e1-4ae3-ae57-8b1e8cf4f141"},"robot_id":"205535"}
    headers = {
        'Content-Type': "application/json"
        }
    response = requests.request("POST", url, json=payload, headers=headers)
    # print(response.text)                  # 打印机器人返回的接口信息
    res = response.json()                   # 调取机器人返回的接口信息的json（字典格式），赋值
    datas = res["result"]["datas"]          # 获取接口信息里，机器人具体回复的内容（在result字典里的datas字典的value键）
    # 调用机器人回复的消息在微信回复
    for i in datas:                         # 遍历机器人具体回复的内容
        print("机器人回答：", i["value"])    # 打印机器人每个回复的内容
        itchat.send_msg(i["value"], toUserName=msg['FromUserName'])         # msg() 前面写发送的内容，后面写发给谁

# 微信自动登录，会生成“itchat.pkl”的文件（加密的，存储的是登录信息）
# 在auto_login()里面提供一个True，即可保留登录状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(hotReload=True)
itchat.run()


'''
# postman发送消息给机器人，机器人返回的接口信息格式
{
    "code":200,
    "msg":"success",
    "result":{
        "app_id":2300101,
        "datas":[
            {
                "data_type":"text",
                "time_interval":0,
                "value":"说到底"
            },
            {
                "data_type":"text",
                "time_interval":300,
                "value":"你好我也好。"
            },
            {
                "data_type":"text",
                "time_interval":600,
                "value":"大家好才是真好"
            }
        ],
        "intent":"chat",
        "parse_type":3
    }
}
'''



'''
msg格式
{
    'MsgId': '690197735056836583', 
    'FromUserName': '@8b1300d8f1d9182b0b9cfa11a25add73', 
    'ToUserName': '@8b1300d8f1d9182b0b9cfa11a25add73', 
    'MsgType': 1, 
    'Content': '你好', 
    'Status': 3, 
    'ImgStatus': 1, 
    'CreateTime': 1559400076, 
    'VoiceLength': 0, 
    'PlayLength': 0, 
    'FileName': '', 
    'FileSize': '', 
    'MediaId': '', 
    'Url': '', 
    'AppMsgType': 0, 
    'StatusNotifyCode': 0, 
    'StatusNotifyUserName': '', 
    'RecommendInfo': {
        'UserName': '', 
        'NickName': '', 
        'QQNum': 0, 
        'Province': '', 
        'City': '', 
        'Content': '', 
        'Signature': '', 
        'Alias': '', 
        'Scene': 0, 
        'VerifyFlag': 0, 
        'AttrStatus': 0, 
        'Sex': 0, 
        'Ticket': '', 
        'OpCode': 0
    }, 
    'ForwardFlag': 0, 
    'AppInfo': {'AppID': '', 'Type': 0}, 
    'HasProductId': 0, 
    'Ticket': '', 
    'ImgHeight': 0, 
    'ImgWidth': 0, 
    'SubMsgType': 0, 
    'NewMsgId': 690197735056836583, 
    'OriContent': '', 
    'EncryFileName': '', 
    'User': <User: {'MemberList': <ContactList: []>, 'UserName': '@8b1300d8f1d9182b0b9cfa11a25add73', 'City': '广州', 'DisplayName': '', 'PYQuanPin': 'lou', 'RemarkPYInitial': '', 'Province': '广东', 'KeyWord': 'lov', 'RemarkName': '', 'PYInitial': 'L', 'EncryChatRoomId': '', 'Alias': '', 'Signature': '', 'NickName': '露', 'RemarkPYQuanPin': '', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=678451688&username=@8b1300d8f1d9182b0b9cfa11a25add73&skey=@crypt_5ecdd477_f476e190eb03e301999df32e9e872445', 'UniFriend': 0, 'Sex': 2, 'AppAccountFlag': 0, 'VerifyFlag': 0, 'ChatRoomId': 0, 'HideInputBarFlag': 0, 'AttrStatus': 21206311, 'SnsFlag': 17, 'MemberCount': 0, 'OwnerUin': 0, 'ContactFlag': 2053, 'Uin': 1934793140, 'StarFriend': 0, 'Statues': 0, 'WebWxPluginSwitch': 0, 'HeadImgFlag': 1, 'IsOwner': 0}>, 
    'Type': 'Text', 
    'Text': '你好'
}
'''


'''
# msg["User"]格式：
{
    'MemberList': <ContactList: []>, 
    'UserName': '@8b1300d8f1d9182b0b9cfa11a25add73', 
    'City': '广州', 
    'DisplayName': '', 
    'PYQuanPin': 'lou', 
    'RemarkPYInitial': '', 
    'Province': '广东', 
    'KeyWord': 'lov', 
    'RemarkName': '', 
    'PYInitial': 'L', 
    'EncryChatRoomId': '', 
    'Alias': '', 
    'Signature': '', 
    'NickName': '露', 
    'RemarkPYQuanPin': '', 
    'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=678451688&username=@8b1300d8f1d9182b0b9cfa11a25add73&skey=@crypt_5ecdd477_f476e190eb03e301999df32e9e872445', 
    'UniFriend': 0, 
    'Sex': 2, 
    'AppAccountFlag': 0, 
    'VerifyFlag': 0, 
    'ChatRoomId': 0, 
    'HideInputBarFlag': 0, 
    'AttrStatus': 21206311, 
    'SnsFlag': 17, 
    'MemberCount': 0, 
    'OwnerUin': 0, 
    'ContactFlag': 2053, 
    'Uin': 1934793140, 
    'StarFriend': 0, 
    'Statues': 0, 
    'WebWxPluginSwitch': 0, 
    'HeadImgFlag': 1, 
    'IsOwner': 0
}
'''


'''
# 微信好友信息格式
{
    'MemberList': <ContactList: []>, 
    'Uin': 0, 
    'UserName': '@8f4096982ec786a5f8472e17e663fc21', 
    'NickName': '�lzzz良 �', 
    'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=691539100&username=@8f4096982ec786a5f8472e17e663fc21&skey=@crypt_5ecdd477_d1eca75a070bce8d53841005c832b79a', 
    'ContactFlag': 2115, 
    'MemberCount': 0, 
    'RemarkName': '良', 
    'HideInputBarFlag': 0, 
    'Sex': 1, 
    'Signature': 'take me as I am', 
    'VerifyFlag': 0, 
    'OwnerUin': 0, 
    'PYInitial': '?LZZZL?', 
    'PYQuanPin': '?lzzzliang?', 
    'RemarkPYInitial': 'L', 
    'RemarkPYQuanPin': 'liang', 
    'StarFriend': 1, 
    'AppAccountFlag': 0, 
    'Statues': 0, 
    'AttrStatus': 16912615, 
    'Province': '广东', 
    'City': '东莞', 
    'Alias': '', 
    'SnsFlag': 17, 
    'UniFriend': 0, 
    'DisplayName': '', 
    'ChatRoomId': 0, 
    'KeyWord': 'LZL', 
    'EncryChatRoomId': '', 
    'IsOwner': 0
}
'''