import itertools

N, K = map(int, input().split())
Tlist = [list(map(int, input().split())) for i in range(N)]

count = 0
for Tflglist in list(itertools.permutations(range(1,N))): #順列
    time = Tlist[0][Tflglist[0]]
    for i in range(1,N-1):
        time += Tlist[Tflglist[i-1]][Tflglist[i]]
    time += Tlist[Tflglist[N-2]][0]
    if time == K:
        count += 1

print(count)
