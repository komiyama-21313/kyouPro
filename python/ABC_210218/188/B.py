N = int(input())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

sumAB = 0
for i in range(N):
    sumAB += A_list[i] * B_list[i]

if sumAB == 0:
    print("Yes")
else:
    print("No")