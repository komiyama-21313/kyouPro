N = int(input())
S = str(input())
Q = int(input())

TAB_list = [list(map(int, input().split())) for _ in range(Q)]

S_list = list(map(str, S))
S1_list = S_list[:N]
S2_list = S_list[N:2*N]

flg = 0
for T, A, B in TAB_list:
    A = A-1
    B = B-1

    if T == 1:
        if flg % 2 == 0:
            if A >= N:
                SA = S2_list[A-N]
                SB = S2_list[B-N]
                S2_list[B-N] = SA
                S2_list[A-N] = SB
            elif B >= N:
                SA = S1_list[A]
                SB = S2_list[B-N]
                S2_list[B-N] = SA
                S1_list[A] = SB
            else:
                SA = S1_list[A]
                SB = S1_list[B]
                S1_list[B] = SA
                S1_list[A] = SB
        else:
            if A >= N:
                SA = S1_list[A-N]
                SB = S1_list[B-N]
                S1_list[B-N] = SA
                S1_list[A-N] = SB
            elif B >= N:
                SA = S2_list[A]
                SB = S1_list[B-N]
                S1_list[B-N] = SA
                S2_list[A] = SB
            else:
                SA = S2_list[A]
                SB = S2_list[B]
                S2_list[B] = SA
                S2_list[A] = SB

    elif T == 2:
        flg += 1

if flg % 2 == 1:
    S_list = S2_list + S1_list
else:
    S_list = S1_list + S2_list

print(''.join(S_list))