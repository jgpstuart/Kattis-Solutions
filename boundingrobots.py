width, length = [int(x) for x in input().split()]

while width > 0 and length > 0:
    tests = int(input())
    width -= 1
    length -= 1
    apx = 0
    apy = 0
    ipx = 0
    ipy = 0
    while tests != 0:
        direction, distance = [x for x in input().split()]
        distance = int(distance)
        if direction == "u":
            ipy += distance
            if apy + distance <= length:
                apy += distance
            else:
                apy = length
        if direction == "d":
            ipy -= distance
            if apy - distance >= 0:
                apy -= distance
            else:
                apy = 0
        if direction == "r":
            ipx += distance
            if apx + distance <=  width:
                apx += distance
            else:
                apx = width
        if direction == "l":
            ipx -= distance
            if apx - distance >= 0:
                apx -= distance
            else:
                apx = 0
        tests -= 1
    print("Robot thinks " + str(ipx) + " " + str(ipy))
    print("Actually at " + str(apx) + " " + str(apy))
    print("")
    width, length = [int(x) for x in input().split()]
