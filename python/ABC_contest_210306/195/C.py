N = int(input())

count = 0
for i in range(1,6):
    if N >= 10**(3*i):
        count += N - 10**(3*i) + 1

print(count)