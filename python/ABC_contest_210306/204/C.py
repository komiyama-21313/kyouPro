n, m = map(int, input().split())

ABs = [list(map(int,input().split())) for _ in range(m)]

out = 0

lset = [set()*n]

for x in range(m):
    lset[ABs[x][0]].add(ABs[x][1])

for s in range(100):
    for x in range(m):
        lset[ABs[x][0]] = lset[ABs[x][0]] | lset[ABs[x][1]]

