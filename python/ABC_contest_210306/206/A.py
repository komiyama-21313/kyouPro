a, b, c = map(int,input().split())
al = a+b+c
print(al-min(a,min(b,c)))