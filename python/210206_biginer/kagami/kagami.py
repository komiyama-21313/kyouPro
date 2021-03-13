N = int(input())
list_di = [input() for x in range(N)]

list_tmp = []
list_kagami = [x for x in list_di if x not in list_tmp and not list_tmp.append(x)]

print (len(list_kagami))