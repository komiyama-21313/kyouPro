N = int(input())

N_list = list(map(int, str(N)))

k = len(N_list)

flg = 0
if k == 1:
    if N_list[0] % 3 == 0:
        print("0")
    else :
        print("-1")
elif k == 2:
    if sum(N_list) % 3 == 0:
        print("0")
    elif N_list[0] % 3 == 0 or N_list[1] % 3 == 0:
        print("1")
    else :
        print("-1")

elif sum(N_list) % 3 == 0:
    print("0")
elif sum(N_list) % 3 == 1:
    for i in N_list:
        if i % 3 == 1:
            print("1")
            flg = 1
            break
    if flg == 0:
        count = 0
        for i in N_list:
            if i % 3 == 2:
                count = count + 1
                if count == 2:
                    print("2")
                    flg = 1
                    break
        if flg == 0:
            print("-1")
else :
    for i in N_list:
        if i % 3 == 2:
            print("1")
            flg = 1
            break
    if flg == 0:
        count = 0
        for i in N_list:
            if i % 3 == 1:
                count = count + 1
                if count == 2:
                    print("2")
                    flg = 1
                    break
        if flg == 0:
            print("-1")
