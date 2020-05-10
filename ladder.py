from math import *

height, angle = [int(x) for x in input().split()]

hypnotoad = height / sin(radians(angle))

answer = ceil(hypnotoad)

print(answer)
