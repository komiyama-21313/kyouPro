def g2(x):
    x_list = list(map(int, str(x)))
    x_list.sort()
    out = ""
    for a in x_list:
        out += str(a)
    return int(out)

def g1(x):
    x_list = list(map(int, str(x)))
    x_list.sort(reverse=True)
    out = ""
    for a in x_list:
        out += str(a)
    return int(out)

def f(x):
    return g1(x) - g2(x)

def f_roop(x, n):
    if n != 0:
        return f_roop(f(x), n-1)
    else:
        return x

N, K = map(int, input().split())

answer = f_roop(N,K)

print(answer)