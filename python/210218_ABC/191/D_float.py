X, Y, R = map(float, input().split())

Y_max = Y + R
Y_min = Y - R

if Y_max >= 0:
    Y_max = int(Y_max)
else :
    Y_max = int(Y_max) - 1
if Y_min > 0:
    Y_min = int(Y_min) + 1
else :
    Y_min = int(Y_min)

count = 0
for y in range(Y_min,Y_max+1):
    X_min = X - pow(R**2 - (float(y) - Y)**2, 0.5)
    X_max = X + pow(R**2 - (float(y) - Y)**2, 0.5)
    if X_max >= 0:
        X_max = int(X_max)
    else :
        X_max = int(X_max) - 1
    if X_min > 0:
        X_min = int(X_min) + 1
    else :
        X_min = int(X_min)
    count += (X_max - X_min) + 1

print(count)