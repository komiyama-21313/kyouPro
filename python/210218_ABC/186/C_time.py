import time


N = int(input())
t1 = time.time()

count = 0
for i in range(N):
    N8 = oct(i+1)
    N_str = list(map(str,str(i+1)))
    N8_str = list(map(str,str(N8)))
    if N_str.count("7") !=0 or N8_str.count("7") != 0:
        count += 1 

print(N - count)

t2 = time.time()

elapsed_time = t2 -t1

print(elapsed_time)