N = int(input())

list_2d = [list(map(int,input().split())) for i in range(N)]
list_0 = [0, 0, 0]
list_2d.insert(0, list_0)

flg = 0
for i in range(N):
  dt = abs(list_2d[i][0] - list_2d[i+1][0])
  dx = abs(list_2d[i][1] - list_2d[i+1][1])
  dy = abs(list_2d[i][2] - list_2d[i+1][2])
  dxy = dx + dy
  if (dt >= dxy) and (dt - dxy) % 2 == 0:
    continue
  else:
    flg = 1
    break

if flg:
  print("No")
else:
  print("Yes")