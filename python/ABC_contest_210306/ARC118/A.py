t, n = map(int, input().split())

x = 100*n // t

if 100*n % t == 0:
    print(x + n - 1)

else :
    print(x+1+n-1)