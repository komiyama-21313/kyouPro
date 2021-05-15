N = int(input())

TS = []
for i in range(N):
    S, T = map(str,input().split())
    T = int(T)
    TS.append([T,S])

TS.sort(reverse=True)

print(TS[1][1])