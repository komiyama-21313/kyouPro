N = int(input())

upperOut_list, lowerOut_list = [], []

i = 1
while i*i <= N:
    if N % i == 0:
        lowerOut_list.append(i)
        if i*i != N:
            upperOut_list.append(N//i)
    i = i+1

[print(i) for i in lowerOut_list+upperOut_list[::-1]]