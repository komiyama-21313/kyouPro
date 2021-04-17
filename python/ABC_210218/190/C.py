import itertools

N, M = map(int, input().split())
AB2d = [list(map(int, input().split())) for i in range(M)]
K = int(input())
C_list, D_list = [], []
#for i in range(K):
#    C, D = map(int, input().split())
#    C_list.append(C)
#    D_list.append(D)
CD2d = [list(map(int, input().split())) for i in range(K)]

ans = 0
#CD2d = [[C,D] for C in C_list for D in D_list]
CD2dlist = list(itertools.product(*CD2d))
for balls in CD2dlist:
    balls = set(balls)
    count = sum(A in balls and B in balls for A,B in AB2d)
    if ans < count:
        ans = count

print(ans)

