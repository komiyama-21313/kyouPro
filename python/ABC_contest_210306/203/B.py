N, K = map(int,input().split())

out = 0
for i in range(1,N+1):
    for j in range(1,K+1):
        x = 100*i + j
        out += x
    
print(out)