for i in range(2,100000):
    x = i
    if x % 2 == 0:
        x = x // 2
    else:
        x = x - 1
    if x % 5 == 0:
        x = x // 5
    else:
        x = x - 1
    if x % 7 == 0:
        x = x // 7
    else:
        x = x - 1
    if x == 6:
        print(i)