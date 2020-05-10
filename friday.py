tests = int(input())


for i in range(tests):
    answer = 0
    startday = 0
    total_days, months = [int(x) for x in input().split()]
    calendar = [int(x) for x in input().split()]
    for j in range(months):
        days = calendar[j]
        if days >= 13 and startday == 0:
            answer += 1
        startday = (startday +(days % 7)) % 7
        total_days -= days
        if total_days <=0:
            break
    print(answer)
