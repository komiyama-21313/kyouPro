n = int(input())

Ds = [list(map(int,input().split())) for _ in range(n)]

for i in range(2,n):
    if Ds[i][0] == Ds[i][1]:
        if Ds[i-1][0] == Ds[i-1][1]:
            if Ds[i-2][0] == Ds[i-2][1]:
                print("Yes")
                exit()
print("No")