N, X = map(int,input().split())

VP_2dlist = [list(map(int, input().split())) for i in range(N)]

X = X * 100
alc_tak = 0.0
count = 0
for V, P in VP_2dlist:
    count += 1
    alc = V * P
    alc_tak += alc
    if alc_tak > X:
        print(count)
        exit()
print("-1")