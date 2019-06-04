'''
题目1：
现在我们有一个班的同学的成绩，以数组形式体现出来。
[88,98,67,54,65,54,98,34,56,78,46,77,33,44,55,66]
现在我们要把80分以上的成绩单独的存放，80分以下的单独的存放成两个不同的数组。
并且输出两个数组。
'''

'''
写法1：
score = [88,98,67,54,65,54,98,34,56,78,46,77,33,44,55,66]
high_score = []
low_score = []
for i in score:
    if i >= 80:
        high_score.append(i)
    else:
        low_score.append(i)
print("80分及以上的成绩：", high_score)
print("80分以下的成绩：", low_score)
'''

'''
写法2：
def fenzu(a):
    score = [88,98,67,54,65,54,98,34,56,78,46,77,33,44,55,66]
    high_score = []
    low_score = []
    for i in score:
        if i >= a:
            high_score.append(i)
        else:
            low_score.append(i)
    print("{}分及以上的成绩：".format(a), high_score)
    print("{}分以下的成绩：".format(a), low_score)

fenzu(50)
'''

# 写法3：

def fangfa(c,k):
    high_score = []
    low_score = []
    for i in c:
        if i >= k:
            high_score.append(i)
        else:
            low_score.append(i)
    print(k, "分及以上：", high_score)
    print(k, "分以下：", low_score)

if __name__ == "__main__":
    c = [88,98,67,54,65,54,98,34,56,78,46,77,33,44,55,66]
    k = 80
    fangfa(c,k)
