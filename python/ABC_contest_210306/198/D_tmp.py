S1 = str(input())
S2 = str(input())
S3 = str(input())

SSS = S1+S2+S3

count_abc_list = []
for i in range(97, 123):
    count_abc_list.append([SSS.count(chr(i)),chr(i)])

varabc = 0
for i in range(len(count_abc_list)):
    if count_abc_list[i][0] != 0:
        varabc += 1

if(varabc > 10):
    print("UNSOLVABLE")
    exit()

abcmap = sorted(count_abc_list, reverse=True)

