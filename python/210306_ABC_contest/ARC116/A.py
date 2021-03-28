T = int(input())

case = [int(input()) for i in range(T)]

for num in case:
    if num==2:
        print("Same")
    elif num == 1:
        print("Odd")
    elif num%4 == 0:
        print("Even")
    elif num%2 == 0:
        print("Same")
    else:
        print("Odd")

