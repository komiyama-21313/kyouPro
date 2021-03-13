N = int(input())

A_list = list(map(int, input().split()))

leftMax = max(A_list[0:2**(N-1)])
rightMax = max(A_list[2**(N-1):2**N])

if leftMax > rightMax:
    print(A_list.index(rightMax)+1)
else :
    print(A_list.index(leftMax)+1)
