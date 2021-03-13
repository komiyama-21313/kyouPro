N, C = map(int, input().split())

abc_list = []
for i in range(N):
    a, b , c = map(int, input().split())
    abc_list.append([a, c])
    abc_list.append([b+1, -c])

abc_list.sort()

money = 0
c_sum = 0
for i in range(2*N-1):
    c_sum += abc_list[i][1]
    time = abc_list[i+1][0] - abc_list[i][0]
    money += min(c_sum, C) * time

print(money)