N = int(input())

rlist = []
Asum = 0
for i in range(N):
    A, B = map(int,input().split())
    rlist.append(2*A+B)
    Asum += A

rlist.sort(reverse=True)

Bpls = 0
ans = 0
for r in rlist:
    Bpls += r
    ans += 1
    if Bpls > Asum:
        print(ans)
        exit()
