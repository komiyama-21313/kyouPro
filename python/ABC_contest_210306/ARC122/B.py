n = int(input())

As = list(map(int,input().split()))

As2 = []
for a in As:
    As2.append(a/2.0)

As2.sort()

if n%2 == 1:
    x = As2[n//2]
elif n%2 == 0:
    x = (As2[n//2-1] + As2[n//2])/2.0

out = 0
for i in range(n):
    out += x + As[i] - min(As[i],x*2)

out /= n

print(out)