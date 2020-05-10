num, denom = [int(x) for x in input().split()]

while num != 0 and denom != 0:
    whole = num // denom
    top = num - whole * denom
    print(str(whole) + " " + str(top) + " / " + str(denom))
    num, denom = [int(x) for x in input().split()]
