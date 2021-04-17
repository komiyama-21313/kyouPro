N = int(input())

AB2d = list(list(map(int, input().split())) for i in range(N))

Asum, Bsum = 0, 0
for i in range(N):
    Asum += AB2d[i][0]
    Bsum += AB2d[i][1]

res_list = []
for i in range(N):
    res = 2*AB2d[i][0] + AB2d[i][1]
    res_list.append(res)

res_list.sort(reverse=True)

count = 0
nokori = Asum
for i in res_list:
    nokori -= i
    count += 1
    if nokori < 0:
        print(count)
        exit()