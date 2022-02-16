for i in range(101,10000):
    x = i
    x = bin(n)[2:]
    if x.count('0') == x.count('1'):
        x = x + str(x % 10)
    else:
        if x.count('0') < x.count('1'):
            x = x + '0'
        else:
            x = x + '1'
        x = int(x, base = 10)
        if x % 2 ==0 and x%4 !=0:
            print(x)
            break