d1, d2 = [int(x) for x in input().split()]

possibilities = []

for i in range(1, d1+1):
    for j in range(1, d2+1):
        possibilities.append(i + j)

most_likely = []
counter = 0
for i in range(len(possibilities)):
    count = possibilities.count(i)
    if count > counter:
        most_likely = []
        most_likely.append(i)
        counter = count
    elif count == counter:
        most_likely.append(i)
    else:
        continue

for i in range(len(most_likely)):
    print(most_likely[i])
