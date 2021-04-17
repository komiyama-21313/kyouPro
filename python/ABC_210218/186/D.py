N = int(input())
A_list = list(map(int, input().split()))

A_list.sort(reverse=True)

result = 0
for i in range(N-1):
    result += (N-i-1)*A_list[i]

for i in range(N-1):
    result -= (N-i-1) * A_list[N-i-1]

print(result)

