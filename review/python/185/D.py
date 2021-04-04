N , M = map(int, input().split())

if M == 0:
    print("1")
    exit()

A_list = list(map(int, input().split()))
A_list.sort()

Ar = []
Ar.append(A_list[0] - 1)
for i in range(M-1):
    Ar.append(A_list[i+1] -1 - A_list[i])
Ar.append(N-A_list[M-1])

xxx = [n for n in Ar if n != 0]
if xxx:
    k = min([n for n in Ar if n != 0])
else:
    print("0")
    exit()

count = 0
for i in Ar:
    if i%k == 0:
        count += i//k
    else:
        count += i//k + 1

print(count)