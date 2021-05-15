n = int(input())

A = 2*3
B = 2*5
C = 3*5

outlist = [[A,A,2],[B,B,2],[C,C,2]]

outputlist = [A,B,C]
while len(outputlist) < n:
    if outlist[0][0] not in outputlist:
        outputlist.append(outlist[0][0])
    outlist[0][0] = outlist[0][1] * outlist[0][2]
    outlist[0][2] += 1
    outlist.sort()

print(*outputlist)
