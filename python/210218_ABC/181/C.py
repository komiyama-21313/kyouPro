def onTheLine(A_list, B_list, C_list):
    x1 = A_list[0]
    y1 = A_list[1]
    x2 = B_list[0]
    y2 = B_list[1]
    x3 = C_list[0]
    y3 = C_list[1]

    if (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2):
        return 1
    else :
        return 0

N = int(input())

input_list = []
for i in range(N):
    tmp_list = list(map(int, input().split()))
    input_list.append(tmp_list)

flg = 0
for i in range(N-2):
    for j in range(N-2-i):
        for n in range(N-2-i-j):
            a_list = input_list[0]
            b_list = input_list[j+1]
            c_list = input_list[n+j+2]
            flg = onTheLine(a_list, b_list, c_list)
            if flg:
                print("Yes")
                exit()
    del input_list[0]
    
print("No")