from math import *

case = [float(x) for x in input().split()]

while case != [0]:
    x1, y1, x2, y2, p = case[0], case[1], case[2], case[3], case[4]
    step1 = abs(x1 - x2)**p + abs(y1 - y2)**p
    step2 = step1 ** (1/p)
    print(step2)
    case = [float(x) for x in input().split()]
