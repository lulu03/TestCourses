yuanzu = (1, 2, 3, 4)
shuzu = [3, 4, 5, 6, 7]

# print("数组", shuzu[4])

zidian = {
    "key": "value",
    "name": "张三",
    "age": 24,
    "high": 167
}

zidian["xuexi"] = "哈哈哈哈"

# print(zidian)

# high = zidian.pop("high")
# print(high)
# print(zidian)

# a = zidian.get("key")
# print(a)


# changdu = len(zidian)
# print(changdu)



# 遍历

shuzu = ["哈哈", "嘻嘻", "哇哇", 4, 5, 6, 7]

# for i in shuzu:
#     print(i)

# 循环100000遍
# 数列生成器

# a = list(range(0, 8))
# print(a)

# for i in range(100000):
#     print(i)

# for i in range(0,1000):
#     print(i)


# print("\n".join([''.join([('LoveTest'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

# i = 0
# while i < 9:
#     i +=1
#     print("哈哈哈哈哈哈")

shuzu = ["哈哈", "嘻嘻", "哇哇", 4, 5, 6, 7]

# for i in shuzu:
#     print(i)


# i = 0
# while i < len(shuzu):
#     print(shuzu[i])
#     i += 1

# 打印出九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i, "*", j, "=", i*j, end="\t")
#     print(" ")

# a = 1 + 2
# if a == 3:
#     print("计算正确！")
# else:
#     print("计算错误！")


hlist = {
    "caoqingshan": {"high":165, "sex": "女"},
    "chenqian": {"high":175, "sex": "女"},
    "gongwei": {"high":161, "sex": "女"},
    "huanghaiyue": {"high":164, "sex": "男"},
    "huangsyhuang": {"high":160, "sex": "女"},
    "lixin": {"high":169, "sex": "女"}
}


# for i in hlist:
#     if hlist[i]["sex"] == "女":
#         print(i)
