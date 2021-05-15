n = int(input())

A = 1
out = 0
while A*A < n:
    B = (n-1)//A
    if B == A:
        out += 1
    else:
        out += 2*(B-(A-1)-1)+1
    A += 1 

print(out)