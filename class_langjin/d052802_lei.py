
'''
包 --> 模块 --> 类 --> 方法 --> 变量

'''


class GirlFriend:
    def __init__(self):
        self.age = 18
        self.high = '165cm'
        self.weight = '50kg'
        self.yanzhi = '7分'
    def zhufan(self, name):
        print("%s会煮饭哦~" % name)
    def nuanchuang(self):
        print("可以暖床哦~")
    def zhengqian(self):
        print("会挣钱养你哦~")






class NewGF(GirlFriend):        # 继承
    def zhufan(self, name):     # 重写
        print("%s会煮饭哦~，还会烧汤！！！" % name)


# GF = GirlFriend("恭维")
# age = GF.age
# print(age)
# GF.zhufan("恭维")



# ngf = NewGF()     # 实例化
# ngf.zhufan("黄爽")
# ngf.nuanchuang()

