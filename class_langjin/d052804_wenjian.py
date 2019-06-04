import time

# rizhi = input("请输入今天的日志：")

# w 写入，每次会创建一个新的文件
# now = time.strftime("%Y-%m-%d-%H-%M-%S")
# print(now)
# with open("./%s日志.txt" % now, "w") as f:      
#     f.write(rizhi)


# a  续写
# with open("./日志.txt", "a") as f:      
#     f.write(rizhi)


# r 读取
with open("./日志.txt", "r") as f:
    aa = f.readlines()
print(aa)
