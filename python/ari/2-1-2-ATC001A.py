import queue
dxdy = ((-1,0),(1,0),(0,-1),(0,1))

h,w = map(int,input().split())
c = [str(input()) for _ in range(h)]

i = 0
for c_l in c:
    sers = c_l.find('s')
    serg = c_l.find('g')
    if sers != -1:
        sx = sers
        sy = i
    if serg != -1:
        gx = serg
        gy = i
    i += 1

visited = [[0]*w for i in range(h)]
q = queue.LifoQueue()
q.put((sx,sy))

while not q.empty():
    x, y = q.get()
    if x == gx and y == gy:#goalならそこでやめる
        print("Yes")
        exit()
    if visited[y][x] == 1:#すでに訪れていた場合
        continue
    visited[y][x] = 1 #訪れたことを記録
    for dx, dy in dxdy:#キューに周囲４方向のセルを追加
        if (0 <= y+dy <= h-1) and (0 <= x+dx <= w-1):#枠内
            if visited[y+dy][x+dx] == 0 and c[y+dy][x+dx] != '#':#壁じゃなくて訪れたことがない 
                q.put((x+dx,y+dy))

print("No")