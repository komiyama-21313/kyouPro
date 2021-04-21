N , M = map(int,input().split())

H_list = list(map(int,input().split()))
W_list = list(map(int,input().split()))

out = 10 ** 11
if N == 1:
    for i in range(M):
        out = min(out, abs(W_list[i]-H_list[0]))
    print(out)
    exit()


H_sort = sorted(H_list)

H_dif = [H_sort[i+1] - H_sort[i] for i in range(N-1)]
H_difodd = [0]*((N-1)//2)
H_difeven = [0]*((N-1)//2)

H_difeven[0] = H_dif[0]
H_difodd[0] = H_dif[1]
for i in range((N-1)//2 - 1):
    H_difeven[i+1] = H_dif[2*(i+1)] + H_difeven[i]
    H_difodd[i+1] = H_dif[2*(i+1)+1] + H_difodd[i]

out = 10**11
j = 0
W_sort = sorted(W_list)
for i in range(M):
    for x in range(j,N):
        if W_sort[i] < H_sort[x]:
            break
        else:
            j += 1
    if j % 2 == 0:
        jchk = j
    else:
        jchk = j-1

    if jchk == 0:
        dist = H_difodd[-1] + abs(H_sort[jchk]-W_sort[i])
    else:
        dist = H_difeven[jchk//2-1] + (H_difodd[-1] - H_difodd[jchk//2-1]) + abs(H_sort[jchk]-W_sort[i])

    out = min(out, dist)

print(out)    