cases = int(input())
for i in range(cases):
    numbers = int(input())
    distances = [int(x) for x in input().split()]
    print((max(distances)-min(distances)) * 2)




