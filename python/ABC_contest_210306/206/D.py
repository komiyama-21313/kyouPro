def angleChk(x1, x2, x3, y1, y2, y3):
    if x1-x2 != 0:
        if x1-x3 != 0:
            if (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2):
                return True 
            else:
                return False
        else:
            return False
    elif x1-x3 != 0:
        return False
    else:
        return True

n = int(input())

abs = [list(map(int,input().split())) for _ in range(n)]
cds = [list(map(int,input().split())) for _ in range(n)]

if n <= 2:
    print("Yes")
    exit()

x = 0
y = 1
flg = 0
for i in range(2, n):
    if angleChk(abs[x][0],abs[y][0],abs[i][0],abs[x][1],abs[y][1],abs[i][1]) == True:
        continue
    else:
        z = i
        flg = 1
        break

if flg == 0:
    for i in range(2,n):
        if angleChk(cds[x][0],cds[y][0],cds[i][0],cds[x][1],cds[y][1],cds[i][1]) == True:
            continue
        else:
            print("No")
            exit()

if flg == 0:
    print("Yes")
    exit()

dis = []
for i in range(n):
    dis_tmp = []
    for j in range(n):
        dis_tmp.append((cds[i][0]-cds[j][0])**2 + (cds[i][1]-cds[j][1])**2)
    dis_tmp.sort()
    dis.append(dis_tmp)

disx = []
disy = []
disz = []
for i in range(n):
    disx.append((abs[i][0]-abs[x][0])**2 + (abs[i][1]-abs[x][1])**2)
    disy.append((abs[i][0]-abs[y][0])**2 + (abs[i][1]-abs[y][1])**2)
    disz.append((abs[i][0]-abs[z][0])**2 + (abs[i][1]-abs[z][1])**2)

disx.sort()
disy.sort()
disz.sort()

flg = 0
xn = 0
for dis_a in dis:
    if dis_a == disx:
        flg = 1
        break
    xn += 1

print(dis)
print(disx)
print(disy)
print(disz)

if flg == 0:
    print("No")
    exit()

flg = 0
yn = 0
for dis_a in dis:
    if dis_a == disy:
        flg = 1
        break
    yn += 1

if flg == 0:
    print("No")
    exit()

flg = 0
zn = 0
for dis_a in dis:
    if dis_a == disz:
        flg = 1
        break
    zn += 1

if flg == 0:
    print("No")
    exit()

if (abs[x][0]>=abs[y][0] and cds[x][0]>=cds[y][0]):
    if abs[x][0]>=abs[z][0] and cds[x][0]>=cds[z][0]:
        print("Yes")
    else:
        print("No")
    
else:
    if abs[x][0]<abs[z][0] and abs[x][0]<abs[z][0]:
        print("Yes")
    else:
        print("No")