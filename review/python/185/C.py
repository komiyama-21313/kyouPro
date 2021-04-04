L = int(input())

up = 1
low = 1
for i in range(11):
    up *= L-1-i
    low *= i+1
print(up//low)