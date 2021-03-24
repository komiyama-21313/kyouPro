def g2(x):
    return int("".join(sorted(str(x))))

def g1(x):
    return int("".join(sorted(str(x))[::-1]))
    #sorted(str)で文字列をソートしたリストを作成
    #str.join() //'間に挿入する文字列'.join([連結したい文字列のリスト])

def f(x):
    return g1(x) - g2(x)

N, K = map(int, input().split())

answer = N
for i in range(K):
    answer = f(answer)

print(answer)