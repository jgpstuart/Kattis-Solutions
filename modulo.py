answer = []
for i in range(10):
    digit = int(input())
    checker = digit % 42
    if checker not in answer:
        answer.append(checker)
print(len(answer))
