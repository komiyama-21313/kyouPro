def oneToSum(num):
    if num % 2 == 0:
        return (1+num)*(num//2)
    else :
        return (1+num-1)*((num-1)//2)+num

N = int(input())

out = 0
for i in range(N):
    a, b = map(int, input().split())
    out = out + oneToSum(b)
    out = out - oneToSum(a-1)

print(out)