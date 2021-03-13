def zyunretuNum(list_inp, int_inp):
    length = len(list_inp)
    i = length
    for j in range(int_inp):
        i = i * (i-j)
    num_out = i
    return num_out

def addlist(list_tmp, list_rest, num, list_2d):
    j = 0
    for i in list_rest:
        list_tmp2 = list_tmp.copy()
        list_tmp2.append(i)
        list_rest2 = list_rest.copy()
        print(list_rest2)
        #print(list_tmp)
        #print(list_2d)
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