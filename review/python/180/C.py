N = int(input())

outset = set()
i = 1
while i*i<=N:
    if N % i == 0:
        outset.add(i)
        outset.add(N//i)
    i += 1

print(*sorted(outset))