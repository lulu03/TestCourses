# a = 1
# b = 2
# c = a + b
# print(c)


# b = 100
# e = 22
# f = b + e
# print(f)


def  jiafa(a,b):
    '''
    这是一个用来计算两个整数相加的方法
    '''
    if type(a) == int and type(b) == int:
        c = a + b
        print(c)
        return c, a
    else:
        print("请输入数字！")


def dayinhahah():
    print("哈哈哈哈哈哈哈哈哈哈哈哈哈")


# 递归
def digui(a):
    b = a / 2
    if b > 10:
        digui(b)
    else:
        print(b)

# digui(2400)

'''
我的手机 2019/5/28 20:40:12
现在我们有一个班的同学的成绩，以数组形式体现出来。
[88,98,67,54,65,54,98,34,56,78,46,77,33,44,55,66]
现在我们要把80分以上的成绩单独的存放，80分以下的单独的存放成两个不同的数组。
并且输出两个数组。
'''

def fenzu(a,b):
    high_score = []
    low_score = []
    for i in a:
        if i >= b:
            high_score.append(i)
        else:
            low_score.append(i)
    print(b, "分及以上的成绩：", high_score)
    print(b, "分以下的成绩：", low_score)



if __name__ == "__main__":
    a = [88, 98, 67, 54, 65, 54, 98, 34, 56, 78, 46, 77, 33, 44, 55, 66]
    b = 80
    fenzu(a, b)





# def chengjifenzu(a):
#     score = [88,98,67,54,65,54,98,34,56,78,46,77,33,44,55,66]
#     high_score = []
#     low_score = []
#     for i in score:
#         if i >= a:
#             high_score.append(i)
#         else:
#             low_score.append(i)
#     print("%s 分及以上的成绩：" % a, high_score)
#     print("%s 分以下的成绩：" % a, low_score)

def chulisz(l):
    newl = []
    for i in l:
        if type(i) == int:
            newl.append(i)
    return newl



l = ["哈哈哈", 123, "hhkdf", 878, 765, "gfsdgf"]
newl = chulisz(l)
ic = 0
for i in newl:
    ic += i
print(ic)
