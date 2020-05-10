parts, days = [int(x) for x in input().split()]
replaced = []

for i in range(days):
    piece = input()
    if piece not in replaced:
        replaced.append(piece)
    if len(replaced) == parts:
        print(i+1)
        break
if len(replaced) != parts:
    print("paradox avoided")
