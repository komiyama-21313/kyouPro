n = int(input())
XLs = [list(map(int,input().split())) for _ in range(n)]

HMs = []
for X, L in XLs:
    H = X-L
    M = X+L
    HMs.append([H,M])

HMsort = sorted(HMs, key=lambda x: x[1])

count = 1
M_max = HMsort[0][1]
for H,M in HMsort:
    if H >= M_max:
        count += 1
        M_max = M

print(count)