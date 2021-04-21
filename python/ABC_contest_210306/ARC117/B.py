N = int(input())
A_set = set(map(int, input().split()))
A_list = list(sorted(A_set))

A_deflist = []
A_deflist.append(A_list[0])
for i in range(len(A_list)-1):
    A_deflist.append(A_list[i+1]-A_list[i])

out = 1
for dif in A_deflist:
    out *= (dif+1)
    out = out%(10**9+7)

print(out)