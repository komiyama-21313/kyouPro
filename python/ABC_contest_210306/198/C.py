R, X, Y = map(int, input().split())

R2 = R**2
XY = X**2 + Y**2

A1 = XY // R2
A2 = XY % R2

if A1 == 0:
    print("2")
    exit()

i = 1
if A2 == 0:
    while i > 0:
        if i**2 >= A1:
            break
        i += 1
    print(i)

else:
    while i > 0:
        if i**2 > A1:
            break
        i += 1
    print(i)