switches = input()
position = [1, 0, 0]

for i in range(len(switches)):
    if switches[i] == "A":
        positiontemp = position[0]
        position[0] = position[1]
        position[1] = positiontemp
    elif switches[i] == "B":
        positiontemp = position[1]
        position[1] = position[2]
        position[2] = positiontemp
    else:
        positiontemp = position[0]
        position[0] = position[2]
        position[2] = positiontemp

if position == [1, 0, 0]:
    print("1")
elif position == [0, 1, 0]:
    print("2")
else:
    print("3")
