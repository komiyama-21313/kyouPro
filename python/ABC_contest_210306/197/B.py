H , W , X , Y = map(int, input().split())

Shw = [list(map(str, str(input()))) for i in range(H)]

count = 1

i = X - 1
j = Y - 1
while i > 0:
    i = i - 1
    if Shw[i][j] != "#":
        count += 1
    else:
        break

i = X - 1
j = Y - 1
while j > 0:
    j = j - 1
    if Shw[i][j] != "#":
        count += 1
    else:
        break

i = X - 1
j = Y - 1
while i < H-1:
    i = i + 1
    if Shw[i][j] != "#":
        count += 1
    else:
        break

i = X - 1
j = Y - 1
while j < W-1:
    j = j + 1
    if Shw[i][j] != "#":
        count += 1
    else:
        break

print(count)