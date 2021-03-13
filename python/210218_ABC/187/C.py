N = int(input())

S_set = set(str(input()) for i in range(N))

for i in S_set:
    if "!"+i in S_set:
        print(i)
        exit()

print("satisfiable")