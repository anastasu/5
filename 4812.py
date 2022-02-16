for n in range(10000000,100000000):
    n_s = str(n)
    s1 = 0
    s2 = 0
    for i in range(1, len(n_s)+1):
        if int(n_s[i-1]) % 2 != 0:
            s1 += int(n_s[i-1])
        if i % 2 == 0:
            s2 += int(n_s[i-1])
    if abs(s1-s2) == 29:
        print(n)
        break