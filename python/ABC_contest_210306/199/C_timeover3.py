N = int(input())
S = str(input())
Q = int(input())

TAB_list = [list(map(int, input().split())) for _ in range(Q)]

S_list = list(map(str, S))
S1_list = S_list[:N]
S2_list = S_list[N:2*N]

for T, A, B in TAB_list:
    A = A-1
    B = B-1
    if T == 1:
        SA_tmp = S_list[A]
        S_list[A] = S_list[B]
        S_list[B] = SA_tmp
    elif T == 2:
        S1_list = S_list[:N]
        S2_list = S_list[N:2*N]
        S_list = S2_list + S1_list
print(''.join(S_list))