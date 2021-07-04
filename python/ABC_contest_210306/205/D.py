n, q = map(int,input().split())

As = list(map(int,input().split()))

Ks = []
for i in range(q):
    K = int(input())
    Ks.append([K, int(i), 0])

Asdiff = [As[0]-1]
Asdsum = [As[0]-1]
for i in range(n-1):
    Asdiff.append(As[i+1]-As[i]-1)
    Asdsum.append(Asdsum[i]+Asdiff[i+1])

As.insert(0,0)
ind = 0
Ks.sort(key=lambda x: x[0])
flg = True
iout = len(Ks)
for i in range(len(Ks)):
    K = Ks[i][0]
    while flg == True:
        if Asdsum[ind] >= K:
            Ks[i][2] = As[ind] + (Asdiff[ind]-(Asdsum[ind]-K))
            break
        else:
            ind += 1
            if ind == n:
                flg = False
    if flg == False:
        iout = i
        break

for i in range(iout, len(Ks)):
    K = Ks[i][0]
    Ks[i][2] = As[ind] + K - Asdsum[ind-1]

Ks.sort(key=lambda x: x[1])
for i in range(q):
    print(Ks[i][2])