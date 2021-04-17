def point(gomoji):
    out = 0
    for i in range(1,10):
        ct = gomoji.count(str(i))
        out += i*10**ct
    return out

K = int(input())
S = str(input())
T = str(input())

rest = []
for i in range(1,10):
    rest.append(K-S.count(str(i))-T.count(str(i)))

count = 0
#takahashi
for i in range(1,10):
    rest_in = rest.copy()
    if rest_in[i-1] - 1 >= 0:
        rest_in[i-1] -= 1
        #aoki
        for j in range(1,10):
            if rest_in[j-1] - 1 >= 0:
                rest_in[j-1] -= 1
                S_in = S.replace('#', str(i))
                T_in = T.replace('#', str(j))
                if point(S_in) - point(T_in) > 0:
                    if i == j:
                        count += rest[i-1] * (rest[j-1] - 1)
                    else:
                        count += rest[i-1] * rest[j-1]

sousu = (K*9-8) * (K*9-8-1)
print(count/sousu)
