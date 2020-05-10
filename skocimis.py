positions = [int(x) for x in input().split()]
jumps = 0

while (positions[2] != positions[1] + 1) or (positions[1] != positions[0] + 1):
    if ((positions[1] - positions[0]) >= (positions[2]-positions[1])):
        positions[2] = positions[0]+1
        jumps += 1
        positions.sort()
    else:
        positions[0] = positions[2]-1
        jumps += 1
        positions.sort()

print(jumps)
