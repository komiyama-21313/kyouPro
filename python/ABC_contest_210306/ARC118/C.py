n = int(input())

A = 2*3*5*7
B = 2*3*5*11
C = 2*3*7*11
D = 2*5*7*11
E = 3*5*7*11

outlist = [[A,A,2],[B,B,2],[C,C,2],[D,D,2],[E,E,3]]

for i in range(n):
    print(outlist[0][0],end=' ')
    outlist[0][0] = outlist[0][1] * outlist[0][2]
    outlist[0][2] += 1
    outlist.sort()

print()