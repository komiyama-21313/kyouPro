C = 10**9 + 7

n = int(input())

As = list(map(int, input().split()))

if n == 1:
    print(As[0])
    exit()

ks = [0]*(n+1)
ks[0] = 1
ks[1] = 1
ks[2] = 2
a = 1
b = 2
for i in range(1,n-1):
    c = a+b
    c = c%C
    ks[i+2] = c
    a = b
    b = c

k = ks[n]

out = As[0]*k % C

for i in range(1,n):
    out += As[i] * ( ks[n-i] * ks[i] - ks[n-1-i]*ks[i-1] ) % C

out %= C

print(out)