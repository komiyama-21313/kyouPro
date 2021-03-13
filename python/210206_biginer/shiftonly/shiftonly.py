N = int(input())
num = list(map(int, input().split()))
x = 0
n = 0
while x < 1:
  for i in range(N):
    if(num[i]%2 == 1):
      x = x+1
  if(x==0):
    for i in range(N):
      num[i] = num[i]/2
      n = n+1
print(n)