S = str(input())

a = S.count("o")
b = S.count("x")
c = S.count("?")

count = 0
for n1 in range(10-b):
    for n2 in range(10-b):
        for n3 in range(10-b):
            for n4 in range(10-b):
                flg = True
                for x in range(a):
                    if x not in (n1,n2,n3,n4):
                        flg = False
                        break
                if flg == True:
                    count += 1

print(count)