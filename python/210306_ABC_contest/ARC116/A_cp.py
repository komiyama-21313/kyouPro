def yakusuu(num):
    countOdd = 0
    countEven = 0
    i=1
    while i*i < num:
        if num%i == 0:
            if i%2==0:
                countEven+=1
            else:
                countOdd+=1
            if (num//i)%2==0 and i*i!=num:
                countEven+=1
            else:
                countOdd+=1
        i+=1

    if countEven > countOdd:
        return "Even"
    elif countOdd > countEven:
        return "Odd"
    else:
        return "same"

T = int(input())

case = [int(input()) for i in range(T)]

for num in case:
    print(yakusuu(num))

