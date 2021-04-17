Const = 998244353
#Const = 7
N = int(input())
A_list = list(map(int,input().split()))

A_list.sort()
count = 0
for i in range(N):
    A_list[i] = A_list[i]%Const
    count += A_list[i]**2
    count = count%Const
base = 0
for i in range(N-1):
    base += A_list[i]%Const
    base = base%Const
    count += A_list[i+1] * base
    count = count%Const
    base *= 2

print(count)

