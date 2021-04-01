N = str(input())

mod3list = [int(s)%3 for s in N]

sumlist = sum(mod3list)
lenlist = len(mod3list)
find1 = mod3list.count(1)
find2 = mod3list.count(2)

if sumlist % 3 == 0:
    print("0")
elif sumlist % 3 == 1:
    if find1 >= 1 and lenlist >= 2:
        print("1")
    elif find2 >= 2 and lenlist >= 3:
        print("2")
    else:
        print("-1")
elif sumlist % 3 == 2:
    if find2 >= 1 and lenlist >= 2:
        print("1")
    elif find1 >= 2 and lenlist >= 3:
        print("2")
    else:
        print("-1")
else:
    print("-1")