N = int(input())

A_list, B_list = [], []

for i in range(N):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)

A_slist = sorted(A_list)
B_slist = sorted(B_list)

Amin = A_slist[0]
Bmin = B_slist[0]

if A_list.index(Amin) != B_list.index(Bmin):
    out = max(Amin, Bmin)
else:
    out1 = max(A_slist[1], Bmin)
    out2 = max(Amin, B_slist[1])
    out3 = Amin + Bmin
    out = min(out1, out2, out3)

print(out)