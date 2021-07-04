n = int(input())
As = list(map(int, input().split()))

out = 0
for a in As:
    if a >= 10:
       out += a-10

print(out) 