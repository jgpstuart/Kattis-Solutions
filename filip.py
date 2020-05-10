case1, case2 = [x for x in input().split()]
test1 = ""
test2 = ""

for i in range(2, -1, -1):
    test1 += case1[i]
    test2 += case2[i]

if test1 > test2:
    print(test1)
else:
    print(test2)
