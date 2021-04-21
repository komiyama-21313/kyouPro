N = int(input())

#tree = [[[0]]*4]*N
#tree[0][0].append(123)
#for i in range(N-1):
#    A,B = map(int, input().split())
#    print(A)
#   print(tree[A-1][0])
#    tree[A-1][0].append(B-1)
#    tree[B-1][0].append(A-1)

#print(tree)

tree2 = [[1,2,[5,6]],[3,4]]
tree2[0][2].append(7)
print(tree2)