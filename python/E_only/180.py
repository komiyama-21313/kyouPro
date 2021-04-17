N = int(input())

XYZ = [tuple(map(int,input().split())) for i in range(N)]

DP = [[1<<30] * N for i in range(1 << N)]

dlist = [[0] * N for i in range(N)]

for fr in range(N):
    a,b,c = XYZ[fr]
    for to in range(N):
        p,q,r = XYZ[to]
        dlist[fr][to] = abs(p-a)+abs(q-b)+max(0,r-c)

DP[0][0] = 0
for S in range(1 << N):
    for to in range(N):
        if S & 1<<to:
            for frm in range(N):
                    DP[S][to] = min(DP[S][to], DP[S-(1 << to)][frm]+dlist[frm][to])

print(DP[(1<<N)-1][0])