A, B = map(int, input().split())

A_list = list(map(int, str(A)))
B_list = list(map(int, str(B)))

A_sum = sum(A_list)
B_sum = sum(B_list)

if A_sum >= B_sum:
    print(A_sum)
else :
    print(B_sum)