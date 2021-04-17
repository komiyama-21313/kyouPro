N = int(input())

xy2d = []
for i in range(N):
    xylist = list(map(int, input().split()))
    xy2d.append(xylist)

count = 0
for i in range(N):
    for j in range(i+1,N):
        if xy2d[i][0] != xy2d[j][0]:
            a = (xy2d[i][1] - xy2d[j][1]) / (xy2d[i][0] - xy2d[j][0])
            if -1 <= a and a <= 1:
                count += 1

print(count)