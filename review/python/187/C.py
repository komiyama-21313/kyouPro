N = int(input())

S_set = set(str(input()) for i in range(N))

for ss in S_set:
    if "!" + ss in S_set:
        print(ss)
        exit()
        
print("satisfiable")