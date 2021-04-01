N = int(input())

xylist = []
for i in range(N):
    xy = list(map(int, input().split()))
    xylist.append(xy)

for i in range(N):
    x1, y1 = xylist[i][0], xylist[i][1]
    for j in range(i+1,N):
        x2, y2 = xylist[j][0], xylist[j][1]
        for k in range(j+1, N):
            x3, y3 = xylist[k][0], xylist[k][1]
            if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1):
                print("Yes")
                exit()

print("No")
