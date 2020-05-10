moves = 0
pairs = int(input())
pile = [int(x) for x in input().split()]
aux = []

pile.reverse()

while len(pile) != 0:
    aux.append(pile.pop())
    moves += 1
    while True:
        if len(pile) != 0 and len(aux) != 0 and pile[-1] == aux[-1]:
            pile.pop()
            aux.pop()
            moves += 1
        else:
            break
if len(aux) != 0:
    print("impossible")
else:
    print(moves)        
