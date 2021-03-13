N = int(input())

out_list = []
for i in range(N):
    if N % (i+1) == 0:
        out_list.append(i+1)

for i in out_list:
    print(i)