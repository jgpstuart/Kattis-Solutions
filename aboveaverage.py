from statistics import mean
cases = int(input())
for i in range(cases):
    above_average = 0
    data = [int(x) for x in input().split()]
    total = data.pop(0)
    dsize = len(data)
    average = mean(data)
    for j in range(dsize):
        if data[j] > average:
            above_average += 1
    answer = above_average/dsize
    print(str("%.3f" % (answer * 100)) + "%")
