print("----判断闰年----")
temp = input("请输入一个年份：")
while not temp.isdigit():
    temp = input("输入格式错误，请重新输入：")
year = int(temp)
if year % 400 == 0:
    print(year,"是闰年")
else:
    if year % 4 == 0 and year % 100 != 0:
        print(year,"是闰年")
    else:
        print(year,"不是闰年")

