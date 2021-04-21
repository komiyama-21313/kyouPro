A, B = map(int, input().split())

biglist = []
for i in range(1,max(A,B)+1):
    biglist.append(i)

smalllist = []
for i in range(1, min(A,B)):
    smalllist.append(i)

if A>=B:
    outlist = list(map(lambda x : x * -1, smalllist))
    outlist += biglist
else:
    outlist = list(map(lambda x : x * -1, biglist))
    outlist += smalllist

last = -1 * sum(outlist)
outlist.append(last)

print(*outlist)