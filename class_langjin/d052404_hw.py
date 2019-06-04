'''
题目3：
有这么一段字符串【k32j5g3k4j65b345lk6h435lk6jnn234lkjn32l4k5hn3k4lj534k6】，
请通过编程的手段来确认，第一次出现 【字母数字字母】这种排序的位置，是第几位
'''


str1 = "k32j5g3k4j65b345lk6h435lk6jnn234lkjn32l4k5hn3k4lj534k6"
# 遍历字符串
i = 0
while (i+2) < (len(str1)-1):
    i += 1
    # 判断是否【字母数字字母】
    if str1[i].isalpha() and str1[i+1].isdigit() and str1[i+2].isalpha():
        print("第一次出现【字母数字字母】是第%d位" % i)
        break
