H, W, N, M = map(int,input().split())

AB_list = [list(map(int,input().split())) for _ in range(N)]
CD_list = [list(map(int,input().split())) for _ in range(M)]

HW_map = [[0]*W for _ in range(H)]
for C, D in CD_list:
    HW_map[C-1][D-1] = 1

for A, B in AB_list:
    A = A-1
    B = B-1
    if HW_map[A][B] == 2:
        continue

    HW_map[A][B] = 2
    for i in range(1,H+1):
        X = A-i
        Y = B
        if X >=0:
            if HW_map[X][Y] != 1:
                HW_map[X][Y] = 2
            else:
                break
        else:
            break
    for i in range(1,H+1):
        X = A+i
        Y = B
        if X < H:
            if HW_map[X][Y] != 1:
                HW_map[X][Y] = 2
            else:
                break
        else:
            break

for A, B in AB_list:
    A = A-1
    B = B-1
    if HW_map[A][B] == 3 or HW_map[A][B] == 5:
        continue

    HW_map[A][B] += 3
    for i in range(1,W+1):
        X = A
        Y = B-i
        if Y >=0:
            if HW_map[X][Y] != 1:
                HW_map[X][Y] += 3
            else:
                break
        else:
            break
    for i in range(1,W+1):
        X = A
        Y = B+i
        if Y < W:
            if HW_map[X][Y] != 1:
                HW_map[X][Y] += 3
            else:
                break
        else:
            break

out = 0
for HW_tmp in HW_map:
    for HW in HW_tmp:
        if HW == 2 or HW == 3 or HW == 5:
            out += 1

print(out)