tests = int(input())

for i in range(tests):
    calories = int(input())
    drinks = calories / 400
    if calories % 400 != 0:
        drinks += 1
    drinks = int(drinks)
    print(drinks)
