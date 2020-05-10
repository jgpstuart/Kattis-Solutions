cplayer = int(input())
rounds = int(input())
time = 210

for i in range(rounds):
    taken, answer = [x for x in input().split()]
    taken = int(taken)
    time -= taken
    if time <= 0:
        break
    if answer == "T":
        if cplayer == 8:
            cplayer = 1
        else:
            cplayer += 1
print(cplayer)
