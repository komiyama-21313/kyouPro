debag = 0
N = int(input())

A_list = list(map(int,input().split()))

orange = 0
for i in range(N):
    x = A_list[i]
    flg_l = 0
    flg_r = 0
    for j in range(0,i):
        if A_list[i-j-1] < x:
            l = i-j+1
            flg_l = 1
            break
    if flg_l == 0:
        l = 1
    for j in range(i+1,N):
        if A_list[j] < x:
            r = j
            flg_r = 1
            break
    if flg_r == 0:
        r = N
    orange = max(orange, (r-l+1)*x)
    
    if debag:
        print(l,r,x)

print(orange)
