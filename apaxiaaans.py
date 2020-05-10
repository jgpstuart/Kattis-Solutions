name = input()
answer = []

answer.append(name[0])
for i in range(1, len(name)):
    if name[i] != name[i - 1]:
        answer.append(name[i])
concat = ""
for i in range(len(answer)):
    concat += str(answer[i])
print(concat)
