N = int(input())
Alist = list(map(int, input().split()))
Blist = list(map(int, input().split()))

print(max(0, min(Blist) - max(Alist) + 1))