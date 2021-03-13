N = int(input())

A_list = list(map(int, input().split()))

A_max = max(A_list)

out = 2
count = 0
maxCount = 0
for i in range(A_max - 1):
    count = 0
    for j in A_list:
        if j >= i+2:
            if j % (i+2) == 0:
                count = count + 1
    if count > maxCount:
        out = i+2
        maxCount = count

print(out)
        