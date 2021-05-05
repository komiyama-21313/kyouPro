K, S = map(int, input().split())

out = 0
for X in range(0,K+1):
    for Y in range(0,K+1):
        if S <= X + Y + K and X + Y <= S:
            out += 1

print(out)