tests = int(input())

for i in range(tests):
    guests = int(input())
    numbers = [int(x) for x in input().split()]
    for j in range(guests):
        if numbers.count(numbers[j]) != 2:
            print("Case #" + str(i + 1) + ": " + str(numbers[j]))
            break
