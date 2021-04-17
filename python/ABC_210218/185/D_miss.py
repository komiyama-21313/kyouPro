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
if N-A_list[M-1] != 0:
    B_list.append(N - A_list[M-1])


minB = min(B_list)
#print(minB)

upper_list = []
lower_list = []
i = 1
while i*i <= minB:
    if minB % i == 0:
        lower_list.append(i)
        if i*i != minB:
            upper_list.append(minB//i)
    i += 1

minB_list = lower_list+upper_list[::-1]
print(minB_list)

k = 1
for i in minB_list:
    for j in B_list:
        if j % i != 0:
            break
    k = i
print(k)

count = 0
for i in B_list:
    count += i // k
    print(count)

print (count)
print(B_list)