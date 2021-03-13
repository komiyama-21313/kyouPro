N = int(input())
a_list = list(map(int, input().split()))
 
n = float('inf')
 
for i in a_list:
  n = min(n,len(bin(i)) - bin(i).rfind('1') - 1)
print(n)