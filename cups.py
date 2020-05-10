dirbs = []

cups = int(input())
for i in range(cups):
    uinp = tuple(x for x in input().split())
    try:
        colour = uinp[0]
        radius = int(uinp[1])
    except ValueError:
        radius = int(uinp[0])/2
        colour = uinp[1]
    finally:
        dirbs.append((radius, colour))
dirbs = sorted(dirbs)
for i in range(len(dirbs)):
    print(dirbs[i][1])
