N, M = map(int, input().split())

if M == 0:
    print("1")
    exit()

A_list = list(map(int, input().split()))
A_list.sort()

B_list = []
if A_list[0] != 1:
    B_list.append(A_list[0]-1)
for i in range(M-1):
    B_tmp = A_list[i+1] - A_list[i] - 1
    if B_tmp != 0:
        B_list.append(B_tmp)
    #B_list.append(B_tmp)

if N-A_list[M-1] != 0:
    B_list.append(N - A_list[M-1])

if not B_list:
    print("0")
    exit()

k = min(B_list)
#print(minB)

count = 0
for i in B_list:
    count += i // k
    if i % k != 0:
        count += 1

print (count)
