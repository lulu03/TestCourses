'''
题目2：
今天是2019年的5月24日，
请通过编程的手段来确认今天是今年的第几天。
'''


year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
tianshu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 判断是否闰年
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    tianshu[1] = 29
# 判断月份和天数输入是否正确
if month > 12 or day > tianshu[month-1]:
    print("您的输入有误，请重新输入！")
else:
    a = 0
    days = day
    while a < (month-1):
        days = days + tianshu[a]
        a += 1
    print("今天是{}年{}月{}日，是今年的第{}天。" .format(year, month, day, days))

