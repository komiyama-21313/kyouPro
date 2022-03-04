
N = int(input())

divide_number = 10**9+7

multipiler10 = 1
multipiler9 = 1
multipiler8 = 1
for i in range(N):
    multipiler10 = multipiler10 * 10 % divide_number
    multipiler9 = multipiler9 * 9 % divide_number
    multipiler8 = multipiler8 * 8 % divide_number

out = multipiler10 - 2*multipiler9 + multipiler8

if out >= 0:
    print(out%divide_number)
elif out+divide_number >= 0:
    print(out+divide_number)
else:
    print(out+2*divide_number)

