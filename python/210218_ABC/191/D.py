X, Y, R = map(float, input().split())


X1000 = int(X * 1000)
Y1000 = int(Y * 1000)
R1000 = int(R * 1000)

Y_max = Y1000 + R1000
Y_min = Y1000 - R1000

if Y_max >= 0:
    Y_max = Y_max//1000
else :
    Y_max = Y_max//1000 - 1
if Y_min >= 0:
    Y_min = Y_min//1000
else :
    Y_min = Y_min//1000 + 1

print(Y_min)

count = 0
for y in range(Y_min,Y_max+1):
    dX2 = (R1000**2 - ((y*1000) - Y1000)**2)
    dX = dX2 ** 0.5
    X_max = X1000 + dX
    X_min = X1000 - dX
    if X_max >= 0.0:
        X_max = X_max//1000
    else :
        X_max = X_max//1000 - 1
    if X_min >= 0.0:
        X_min = X_min//1000
    else :
        X_min = X_min//1000 + 1

print(count)