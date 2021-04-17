N = int(input())

XYZ = [list(map(int,input().split())) for i in range(N)]

DP = [[int(pow(10,8)) for j in range(N)] for i in range(2**N)]

dlist = []
for frXYZ in XYZ:
    dlist_tmp = []
    a,b,c = frXYZ[0],frXYZ[1],frXYZ[2]
    for toXYZ in XYZ:
        p,q,r = toXYZ[0],toXYZ[1],toXYZ[2]
        dlist_tmp.append(abs(p-a)+abs(q-b)+max(0,r-c))
    dlist.append(dlist_tmp)

DP[0][0] = 0
for S in range(1,2**N):
    for to in range(N):
        if S & 2**to:
            for frm in range(N):
                    DP[S][to] = min(DP[S][to], DP[S-2**to][frm]+dlist[frm][to])

print(DP[2**N-1][0])