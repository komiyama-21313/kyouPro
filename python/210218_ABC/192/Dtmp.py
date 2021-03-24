#Aがn進数のとき10進数で何になるか。
#
def nTo10(A,n):
    A_list = list(map(int, str(A)))[::-1]
    ans = 0
    for i in range(len(A)):
        ans += n**i * A_list[i]
    return ans

X = str(input())
M = int(input())

d = max(list(map(int, X)))

r = d+1
l = int(X)
if l <= r:
    if M >= l:
        print("1")
    else :
        print("0")
else:
    l = M+1
    if l<=r:
        print("0")
        exit()
    xxx = 1
    while xxx > 0:
        mid = (l + r) //2
        if M >= nTo10(X,mid):
            r = mid
        elif M < nTo10(X,mid):
            l = mid
        if l-r == 1:
            l = r
            break
    print(l-d)
