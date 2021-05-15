k, n, m = map(int, input().split())

As = list(map(int, input().split()))

MAs = [0 for _ in range(k)]
nB_Ma = [[0,0] for _ in range(k)]

for i in range(k):
    MAs[i] = As[i] * m
    nB_Ma[i] = [-1*MAs[i],i]

nB_Ma.sort(reverse = True)

stair = sum(nB_Ma)
stairk = k
for i in range(k):
    if stair >= -1*n*k:
        stairk = i
        break
    if i != 0:
        stair += (k-i)*(-1*nB_Ma[i]+nB_Ma[i-1])
    else:
        stair += (k-i)*(-1*nB_Ma[i])


print([stair,stairk])
