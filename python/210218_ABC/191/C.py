def countArround(lu_, ld_, ru_, rd_, lis_, ii, jj):
    if lis_[ii-1][jj-1] == "#":
        lu_ += 1
    if lis_[ii][jj-1] == "#":
        lu_ += 1
        ld_ += 1
    if lis_[ii+1][jj-1] == "#":
        ld_ += 1
    if lis_[ii-1][jj] == "#":
        lu_ += 1
        ru_ += 1
    if lis_[ii+1][jj] == "#":
        ld_ += 1
        rd_ += 1
    if lis_[ii-1][jj+1] == "#":
        ru_ += 1
    if lis_[ii][jj+1] == "#":
        ru_ += 1
        rd_ += 1
    if lis_[ii+1][jj+1] == "#":
        rd_ += 1
    return lu_, ld_, ru_, rd_


H, W = map(int, input().split())

S_hw = [list(map(str, str(input()))) for i in range(H)]

count = 0
for i in range(H):
    for j in range(W):
        if S_hw[i][j] == "#":
            lu, ld, ru, rd = 0, 0, 0, 0
            lu, ld, ru, rd = countArround(lu,ld,ru,rd,S_hw,i,j)
            if lu == 2:
                count += 1
            elif lu == 0:
                count += 3
            if ld == 2:
                count += 1
            elif ld == 0:
                count += 3
            if ru == 2:
                count += 1
            elif ru == 0:
                count += 3
            if rd == 2:
                count += 1
            elif rd == 0:
                count += 3

print(count//3)