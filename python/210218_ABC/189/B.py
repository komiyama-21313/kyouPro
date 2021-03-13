N, X = map(int,input().split())

VP_2dlist = [list(map(int, input().split())) for i in range(N)]

alc_tak = 0.0
count = 0
for V, P in VP_2dlist:
    count += 1
    alc = V * P * 0.01
    alc_tak += alc
    if alc_tak > X:
        print(count)
        exit()
print("-1")