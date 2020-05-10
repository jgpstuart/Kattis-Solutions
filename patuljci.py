numbers = []
total = 0
for i in range(9):
    numbers.append(int(input()))

for i in range(9):
    total = sum(numbers[:7])
    if total == 100:
        break
    else:
        remover = numbers.pop()
        numbers.insert(0, remover)

for i in range(7):
    print(numbers[i])
