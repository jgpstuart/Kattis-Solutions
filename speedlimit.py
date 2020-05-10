total_miles = 0
lasttime = 0
intervals = input()
while int(intervals) > 0:
    for i in range(int(intervals)):
        speed, time = [int(x) for x in input().split()]
        total_miles += speed * (time - lasttime)
        lasttime = time
    print(str(total_miles) + " miles")
    intervals = input()
    total_miles = 0
    lasttime = 0
