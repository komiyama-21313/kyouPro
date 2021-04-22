H, W = map(int, input().split())

S_map = [str(input()) for _ in range(H)]

out_map = [[[0]*4 for _ in range(W+1)] for i in range(H+1)]

X=0
Y=0
out_map[1][1][3] = 1
for SS in S_map:
    X+=1
    Y=0
    for ch in SS:
        Y+=1
        if ch == "#":
            continue
        else:
            out_map[X][Y][0] += out_map[X-1][Y-1][0] + out_map[X-1][Y-1][3]
            out_map[X][Y][1] += out_map[X-1][Y][1] + out_map[X-1][Y][3]
            out_map[X][Y][2] += out_map[X][Y-1][2] + out_map[X][Y-1][3]
            out_map[X][Y][3] += out_map[X][Y][0] + out_map[X][Y][1] + out_map[X][Y][2]
            out_map[X][Y][3] = out_map[X][Y][3]%(10**9+7)

print(out_map[H][W][3])