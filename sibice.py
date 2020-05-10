from math import *

capacity, length, width = [int(x) for x in input().split()]

slant = sqrt(length **2 + width ** 2)

for i in range(capacity):
    match = int(input())
    if match <= slant:
        print("DA")
    elif match <= length or match <= width:
        print("DA")
    else:
        print("NE")
