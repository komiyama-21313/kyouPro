H, W = map(int, input().split())

As = [str(input()) for _ in range(H)]
#As[y][x] ymax = H, xmax = W

dxdy = [[0,1],[1,0]]

countMap = [[0]*W for _ in range(H)]
if (H+W)%2 == 0:#takahasi
    if As[H-1][W-1] == "+":
        countMap[H-1][W-1] = -1
    else:
        countMap[H-1][W-1] = 1
else:
    if As[H-1][W-1] == "+":
        countMap[H-1][W-1] = 1
    else:
        countMap[H-1][W-1] = -1

for yr in range(H):
    y = H-yr-1
    for xr in range(W):
        x = W-xr-1
        if yr == 0 and xr == 0:
            continue
        if (x+y)%2 == 0:#takahashi
            maxCount = -500000
            for dy, dx in dxdy:
                if (y+dy<H) and (x+dx<W):
                    maxCount = max(maxCount, countMap[y+dy][x+dx])
            if As[y][x] == "+":
                countMap[y][x] = maxCount-1
            else:
                countMap[y][x] = maxCount+1
        else:#aoki
            minCount = 500000
            for dy, dx in dxdy:
                if (y+dy<H) and (x+dx<W):
                    minCount = min(minCount, countMap[y+dy][x+dx])
            if As[y][x] == "+":
                countMap[y][x] = minCount+1
            else:
                countMap[y][x] = minCount-1


if As[0][0] == "+":
    countMap[0][0] += 1
else:
    countMap[0][0] -= 1

if countMap[0][0] > 0:
    print("Takahashi")
elif countMap[0][0] < 0:
    print("Aoki")
else :
    print("Draw")
