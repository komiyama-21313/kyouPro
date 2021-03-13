L = int(input())

#L-1 C 11 

under = 1
upper = 1
for i in range(11):
    under *= i+1
    upper *= (L-1)-i

out = upper//under

print(out)