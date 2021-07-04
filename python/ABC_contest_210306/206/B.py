a, b, c, d = map(int,input().split())

if b>=d*c:
    print("-1")
else:
    i = 0
    while a > 0:
        if a+b*i <= d*c*i:
            print(i)
            exit()
        i+=1

