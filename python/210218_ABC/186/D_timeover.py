N = int(input())
A_list = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(N-i-1):
        result += abs(A_list[i] - A_list[j+i+1])

print(result)

