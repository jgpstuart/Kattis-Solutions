tests = int(input())

for i in range(tests):
    set, integer = [int(x) for x in input().split()]
    sone = int((integer * (integer + 1)) / 2)
    stwo = sone * 2 - integer
    sthree = sone * 2
    print(str(set) + " " + str(sone) + " " + str(stwo) + " " + str(sthree))
