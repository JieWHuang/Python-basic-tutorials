def F(n):
    if n < 1:
        print("输入有误！")
        return -1
    if n < 3:
        x = 1
    else:
        x = F(n-1) + F(n-2)
    return x
