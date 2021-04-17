N, M, Q = map(int,input().split())

VW2d = []
for i in range(N):
    W, V = map(int,input().split())
    VW2d.append([V, W])

VW2d.sort(reverse=True)

X1d = list(map(int, input().split()))

LR2d = []
for i in range(Q):
    L, R = map(int, input().split())
    LR2d.append([L, R])

# Quely loop (print each answer)
for i in range(Q):
    X1d_each = X1d.copy()
    L, R = LR2d[i][0], LR2d[i][1]
    del X1d_each[L-1:R]
    X1d_each.sort()
    V_tot = 0
    for V, W in VW2d:
        for j in range(len(X1d_each)):
            if X1d_each[j] >= W:
                V_tot += V
                X1d_each[j] = 0
                break
    print(V_tot)


    