import itertools
a,b,c,d = map(int,input().split())
left = [a,b]
right = [c,d]
xylist2d = list(itertools.product(left,right))
xylist = []
for x,y in xylist2d:
    xylist.append(x*y)
print(max(xylist))