sweet, sour = [int(x) for x in input().split()]

while sweet != 0 or sour != 0:
    if sweet + sour == 13:
        print("Never speak again.")
    elif sweet == sour:
        print("Undecided.")
    elif sweet < sour:
        print("Left beehind.")
    else:
        print("To the convention.")
    sweet, sour = [int(x) for x in input().split()]


