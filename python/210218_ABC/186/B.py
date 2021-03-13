H, W = map(int, input().split())

A_2d = []
for i in range(H):
    A_tmp = list(map(int, input().split()))
    A_2d.append(A_tmp)

Amin = min(list(map(lambda x: min(x), A_2d)))

count = 0
for i in range(H):
    for j in range(W):
        count += A_2d[i][j] - Amin

print(count)