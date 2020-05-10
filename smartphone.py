cases = int(input())

for i in range(cases):
    answer = 10000
    types = 10000
    targetword = input()
    typed = input()
    if typed == targetword:
        answer = 0
    for k in range(len(typed)+1):
        if typed[:k] == targetword[:k]:
            continue
        else:
            types = 0
            types += (len(typed) - (k-1)) + (len(targetword) - (k-1))
            break
    if types == 10000:
        answer = len(targetword) - len(typed)
    if types < answer:
        answer = types

    for j in range(3):
        selectedword = input()
        types = 1
        if selectedword == targetword:
            types = 1
        for k in range(len(selectedword)+1):
            if selectedword[:k] == targetword[:k]:
                continue
            else:
                types += (len(selectedword) - (k-1)) + (len(targetword) - (k-1))
                break
        if types == 1:
            types += len(targetword) - len(selectedword)
        if types < answer:
            answer = types
    print(answer)
