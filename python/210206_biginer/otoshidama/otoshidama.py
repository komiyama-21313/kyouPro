N, Y = map(int, input().split())

flug = False
out = [-1, -1, -1]
for i in range(N+1):
  for j in range(N-i+1):
    if 10000*i + 5000*j + 1000*(N-i-j) == Y:
      out = [i, j, (N-i-j)]
      flug = True
      break
  if flug:
    break
out_line = str(out[0]) + ' ' + str(out[1]) + ' ' + str(out[2])
print(out_line)