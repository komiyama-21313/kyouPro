N = int(input())
A_list = list(map(int, input().split()))

sumlist = []
xxx = 0
for i in range(N):
    xxx += A_list[N-(i+1)]
    sumlist.append(xxx)


out = 0
for i in range(N):
    out += A_list[i] ** 2 * (N-1)

for i in range(N-1):
    out -= 2*A_list[i] * sumlist[N-(i+2)]

print(out)