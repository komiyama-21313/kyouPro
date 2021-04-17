A, B, W = map(int, input().split())

if W*1000 < A:
    print("UNSATISFIABLE")
    exit()

A_num = W*1000 // A
rest = W*1000 - (A_num*A)

sa = B - A

if rest > sa*A_num:
    print("UNSATISFIABLE")
    exit()

if W*1000 < B:
    B_num = 1
elif (W*1000) % B == 0:
    B_num = W*1000 // B
else :
    B_num = W * 1000 // B + 1

print(B_num,A_num)