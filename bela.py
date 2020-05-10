scoring = {
    "AD":11,
    "AND": 11,
    "KD": 4,
    "KND": 4,
    "QD": 3,
    "QND": 3,
    "JD": 20,
    "JND": 2,
    "TD": 10,
    "TND": 10,
    "9D": 14,
    "9ND": 0,
    "8D": 0,
    "8ND": 0,
    "7D": 0,
    "7ND": 0}

games, trump = input().split()
hands = int(games) * 4
points = 0

for i in range(hands):
    check = input()
    card = check[0]
    suit = check[1]
    if suit == trump:
        add = card+"D"
        points += scoring.get(add)
    else:
        add = card+"ND"
        points += scoring.get(add)

print(points)

