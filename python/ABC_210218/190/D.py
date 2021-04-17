N = int(input())

i = 1
count = 0
while i*i <= 2*N:
    if i % 2 == 0:
        if N % i == i/2:
            count += 2
    else :
        if N % i == 0:
            count += 2
    i += 1

print(count)