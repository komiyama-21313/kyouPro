N = int(input())

s = set()
i = 2
while i * i <= N:
    if i not in s:
        j = 2
        while i ** j <= N:
            s.add(i**j)
            j += 1
    i += 1

print(N - len(s))
