s = input()
n = len(s)

ans = 0

for bit in range(1 << (n-1)):#　1<<n は 2^nと等価
    f = s[0]

    for i in range(n-1):
        if bit & (1<<i):# bit演算,bitに+を入れる位置に１が記録されていて、各位置で&をとることでその位置が1なら正が帰る仕組み
            f += "+"
        f += s[i+1]

    ans += sum(map(int, f.split("+")))# 文字列の足し算簡単だから覚える。

print(ans)