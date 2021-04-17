N, S, D = map(int, input().split())
XY2d = [list(map(int, input().split())) for i in range(N)]

for X, Y in XY2d:
    if X < S and Y > D:
        print("Yes")
        exit()
print("No")