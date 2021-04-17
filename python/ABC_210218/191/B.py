N, X = map(int, input().split())

A_list = list(map(int, input().split()))

Adash_list = [A for A in A_list if A != X]

print(*Adash_list)