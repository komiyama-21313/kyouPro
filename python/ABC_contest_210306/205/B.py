n = int(input())

As = list(map(int, input().split()))
As.sort()

for i in range(1,n+1):
    if As[i-1] == i:
        continue
    else:
        print("No")
        exit()
print("Yes")