As = list(map(int,input().split()))

As.sort()

if As[0] - As[1] == As[1] - As[2]:
    print("Yes")
else:
    print("No")
