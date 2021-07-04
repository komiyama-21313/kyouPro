a, b, c = map(int,input().split())

if a == b:
    print("=")
    exit()

if c % 2 == 1:
    if a > b:
        print(">")
        exit()
    else:
        print("<")
        exit()
else:
    if abs(a) > abs(b):
        print(">")
        exit()
    elif abs(a) < abs(b):
        print("<")
        exit()
    else:
        print("=")
        exit()