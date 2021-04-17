S = input()
S = S[::-1]
i=1
while i > 0:
  flg = 1
  for ss in ["dreamer", "dream", "eraser", "erase"]:
    ss = ss[::-1]
    if S.find(ss) == 0:
      S = S.replace(ss, '', 1)
      flg = 0
      break
  if flg:
    break

if len(S) == 0:
  print("YES")
else:
  print("NO")