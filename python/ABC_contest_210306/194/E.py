N, M = map(int, input().split())
A_list = list(map(int, input().split()))

A_set_list = list(set(A_list))
if A_set_list[0] == 0:
    del A_set_list[0]

flg = 0
for i in range(len(A_set_list)):
    if (i+1) != A_set_list[i]:
        mex = i+1
        flg = 1
        break
if flg == 0:
    mex = len(A_set_list) + 1

if N != M:
    mextmp = mex
    min1 = list(A_list[M:])
    min2 = list(A_list[:(N-M)])
    min1set = list(set(min1))
    min2set = list(set(min2))
    print(min1set)
    print(min2set)
    if min1set[0] == 0:
        del min1set[0]
    if min2set[0] == 0:
        del min2set[0]
    if len(min1set) != 0:
        mex = min(mex, min1set[0])
    if len(min2set) != 0:
        mex = min(mex, min2set[0])

print(mex)