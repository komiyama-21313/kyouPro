s = str(input())
t = str(input())

n = len(s)-len(t)+1

# start位置を変えて文字列が一致させられるかをすべて試す。
# 試した結果一致させられたら、ansに格納する。
ans = []
for start in range(n):
    flg = 0
    s_tmp = s
    for moji in range(len(t)):
        if s_tmp[start+moji] == t[moji] or s_tmp[start+moji] == '?':
            pass
        else:
            flg = 1
            break
    if flg == 0:
        # ?を取り除いた文字列にする。一致部分は変換し、それ以外はaにする。
        s_tmp = s_tmp[:start] + t + s_tmp[start+len(t):]
        s_tmp = s_tmp.replace('?','a')
        ans.append(s_tmp)

if not ans:#listが空なら解なし
    print('UNRESTORABLE')
else:#文字列の大小もminで記述できる
    print(min(ans))