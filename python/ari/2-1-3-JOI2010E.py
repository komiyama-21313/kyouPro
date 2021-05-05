import queue
dxdy = ((1,0),(-1,0),(0,1),(0,-1))

h,w,n = map(int, input().split())

MAP = [str(input()) for _ in range(h)]

i = 0
gxgy = [[0]*2 for _ in range(n)]
for c_l in MAP:
    sers = c_l.find('S')
    if sers != -1:
        sx = sers
        sy = i    
    for num in range(1,n+1):
        sernum = c_l.find(str(num))
        if sernum != -1:
            gxgy[num-1] = [sernum,i]
    i += 1

count = 0
for gx, gy in gxgy: # ゴールとスタートを更新して継続
    q = queue.Queue() # キューの中を空にする（定義する）、幅優先なのでQueueとする
    q.put((sx,sy,0)) # (スタートのx座標, スタートのy座標, スタートからの距離（0）)
    visited = [[0]*w for _ in range(h)] # 訪れた場所をリセット

    # 1.訪れることができる点をスタートから近いほうからキューに追加する（無理な点はそもそも追加しない）
    # 2.ゴールなら終了、訪れたことがあれば無視する
    # 3.訪れた場所は記録する
    # キューが空になるまでループする
    while not q.empty():
        x, y, d = q.get()
        if x == gx and y == gy:#ゴールなら終了
            count += d
            break
        if visited[y][x] == 1:#訪れたことがあるなら無視
            continue

        visited[y][x] = 1 # 記録する
        for dx, dy in dxdy: # 四方を考慮
            if (0<=x+dx<=w-1) and (0<=y+dy<=h-1): # 範囲内に限定
                if visited[y+dy][x+dx] == 0 and MAP[y+dy][x+dx] != 'X': # 障害は避ける
                    q.put((x+dx,y+dy,d+1)) # キューに追加

    sx = gx
    sy = gy

print(count)


