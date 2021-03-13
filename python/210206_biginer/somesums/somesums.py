N, A, B = map(int, input().split())

ans = 0
for i in range(1,N+1):
  N_list = list(map(int, list(str(i))))
  sum = 0
  for j in N_list:
    sum = sum + j
  if(sum >= A and sum <= B):
    ans = ans + i
print(ans)