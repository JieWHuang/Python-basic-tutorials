import random
times = 3
secret = random.randint(1,10)
print('------------------小游戏------------------')
guess = 0
print("不妨猜一下1到10里面的随机数字是哪个数字：",end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        temp = input("抱歉，您的输入有误，请输入一个整数：")
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print("猜对了")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
        if times > 0:
            print("再试一次吧：",end=" ")
        else:
            print("机会用完咯")
print("游戏结束，不玩咯")
