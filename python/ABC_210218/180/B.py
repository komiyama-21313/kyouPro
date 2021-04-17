N = int(input())

x_list = list(map(float, input().split()))
x_listabs = list(map(abs,x_list))

d1 = 0.0
d2 = 0.0
d3 = 0.0

for i in x_listabs:
    d1 = d1 + i
    d2 = d2 + i**2

d2 = pow(d2, 0.5)
d3 = max(x_listabs)

print("{0}\n{1}\n{2}".format(d1,d2,d3))