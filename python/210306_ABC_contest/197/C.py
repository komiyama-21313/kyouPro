def Twosin30(Ai_):
    out30 = []
    for i in range(30):
        n = 29 - i
        if Ai_ >= 2**n:
            Ai_ = Ai_ - (2**n)
            k = 1
        else:
            k = 0
        out30.append(k)
    return out30

N = int(input())

A_list = list(map(int, input().split()))

twolist = []
for i in range(N):
    Ai = A_list[i]
    twolist.append(Twosin30(Ai))

print(twolist)