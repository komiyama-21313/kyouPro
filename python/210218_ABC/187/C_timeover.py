N = int(input())

S_list = [str(input()) for i in range(N)]

for i in S_list:
    if "!"+i in S_list:
        print(i)
        exit()

print("satisfiable")