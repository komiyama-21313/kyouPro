N = int(input())
S = str(input())
Q = int(input())

TAB_list = [list(map(int, input().split())) for _ in range(Q)]


for T, A, B in TAB_list:
    A = A-1
    B = B-1
    if T == 1:
        if B != 2*N:
            Stmp = S[:A] + S[B] + S[A+1:B] + S[A] + S[B+1:]
        elif B == 2*N:
            Stmp = S[:A] + S[B] + S[A+1:B] + S[A]
        S = Stmp
    elif T == 2:
        Stmp = S[N:2*N] + S[:N]
        S = Stmp

print(S)