N, X = map(int, input().split())
S = input()

S_list = list(map(str, str(S)))

score = X
for i in range(N):
    if S_list[i] == "o" :
        score += 1
    elif score >= 1 :
        score -= 1

print(score)