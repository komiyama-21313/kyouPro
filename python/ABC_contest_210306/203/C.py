n, k = map(int,input().split())

ABs = [list(map(int,input().split())) for _ in range(n)]
ABs.sort()

money = k
place = 0
for i in range(n):
    if money >= (ABs[i][0]-place):
        money += ABs[i][1] - (ABs[i][0]-place)
        place += (ABs[i][0]-place)
    else:
        place += money
        print(place)
        exit()

place += money
print(place)