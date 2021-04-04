def toOctString(ss):
    outss = ''
    while ss > 0:
        outss = str(ss%8) + outss
        ss //= 8
    return outss

if __name__ == "__main__":
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if "7" not in str(i) and "7" not in toOctString(int(i)):
            count += 1
    print(count)
