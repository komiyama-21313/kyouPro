n = int(input())

tlrs = [list(map(int,input().split())) for _ in range(n)]

tlrs.sort(key=lambda x: x[1])

count = 0
i0 = 1
for t0, l0, r0 in tlrs:
    for i in range(i0,n):
        t1, l1, r1 = tlrs[i]
        if (t0 == 1 or t0 == 3) and (t1 == 1 or t1 == 2):
            if r0 >= l1:
                count += 1
        else:
            if r0 > l1:
                count += 1
    i0 += 1

print(count)