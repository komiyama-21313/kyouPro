def testtt(list_tes):

    for i in range(3):
        list_tes.append(i)
    if len(list_tes) < 10:
        testtt(list_tes)

list_xx = []
for i in range(5):
    testtt(list_xx)

print(list_xx)