debag = 0

N, M, T = map(int, input().split())

list_AB2d = []
for i in range(M):
    list_AB = list(map(int, input().split()))
    list_AB2d.append(list_AB)

if debag:
    print(list_AB2d)

battery = N
battery -= list_AB2d[0][0]
if battery <= 0:
    print("No")
    exit()
for i in range(M-1):
    battery += (list_AB2d[i][1] - list_AB2d[i][0])
    if battery > N:
        battery = N
    battery -= (list_AB2d[i+1][0] - list_AB2d[i][1])
    if battery <= 0:
        print("No")
        exit()

battery += (list_AB2d[M-1][1] - list_AB2d[M-1][0])
if battery > N:
    battery = N
battery -= (T - list_AB2d[M-1][1])

if battery <= 0:
    print("No")
else:
    print("Yes")