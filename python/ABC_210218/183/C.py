def addlist(list_tmp, list_rest, num, list_2d):
    j = 0
    for i in list_rest:
        list_tmp2 = list_tmp.copy()
        list_tmp2.append(i)
        list_rest2 = list_rest.copy()
        del list_rest2[j]

        if len(list_tmp2) == num:
            list_2d.append(list_tmp2)

        else:
            addlist(list_tmp2, list_rest2, num, list_2d)

        j = j+1
    return list_2d


def zyunretu2dList(list_inp, int_inp):
    list_tmp = []
    list_2d = []
    list_out = addlist(list_tmp, list_inp, int_inp, list_2d)
    return list_out
    

N, K = map(int, input().split())

list_T = []
for i in range(N):
    list_T_tmp = list(map(int, input().split()))
    list_T.append(list_T_tmp)

list_inp = list(range(N-1))

list_out = zyunretu2dList(list_inp, N-1)

num_out = 0
for list_chk in list_out:
    p1 = 0
    p2 = list_chk[0] + 1
    time = list_T[p1][p2]
    for i in range(len(list_chk)-1):
        p1 = list_chk[i] + 1
        p2 = list_chk[i+1] + 1
        time = time + list_T[p1][p2]
    p1 = list_chk[-1] + 1
    p2 = 0
    time = time + list_T[p1][p2]
    if time == K:
        num_out = num_out + 1

print(num_out)
