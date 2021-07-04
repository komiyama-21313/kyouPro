n, m = map(int,input().split())

XYs = [list(map(int,input().split())) for _ in range(m)]

XYs.sort(key=lambda x: x[0])

line = {n}
lineadd = set()
linerm = set()
ynow = 0
for X,Y in XYs:
    #print([X,Y])
    if X != ynow:
        line = line - linerm
        line = line|lineadd
        ynow = X
        lineadd = set()
        linerm = set()
    if Y-1 in line:
        lineadd.add(Y)
    if Y+1 in line:
        lineadd.add(Y)
    if Y in line:
        linerm.add(Y)
    #print([line,lineadd,linerm])

line = line - linerm
line = line|lineadd

print(len(line))