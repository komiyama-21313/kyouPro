N = int(input())

APX_list = [list(map(int, input().split())) for i in range(N)]

maxP = 10 ** 9
minP = maxP + 1
for A, P, X in APX_list:
    if X - A > 0:
        minP = min(minP, P)

if minP > maxP:
    minP = -1

print(minP)