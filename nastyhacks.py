tests = int(input())

for i in range(tests):
    base, ads, cost = [int(x) for x in input().split()]
    if (base + cost) == ads:
        print("does not matter")
    elif (base + cost) < ads:
        print("advertise")
    elif (base + cost) > ads:
        print("do not advertise")
