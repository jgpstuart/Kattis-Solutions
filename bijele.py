king, queen, rook, bishop, knight, pawn = [int(x) for x in input().split()]

kians = 1 - king
quans = 1 - queen
roans = 2 - rook
bians = 2 - bishop
knans = 2 - knight
paans = 8 - pawn

print(kians, quans, roans, bians, knans, paans)
