N = int(input())

N_true = str(N)

N_rev = N_true[::-1]

for i in range(10):
    if N_rev == N_true:
        print("Yes")
        exit()
    N_true = "0" + N_true
    N_rev = N_true[::-1]

print("No") 