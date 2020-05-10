length, total_walls = [int(x) for x in input().split()]
walls = [int(x) for x in input().split()]
walls.append(length)
walls.append(0)
answers = []

walls.sort(reverse=True)

for i in range(len(walls)):
    for j in range(i+1, len(walls)):
        answers.append(walls[i] - walls[j])

temporary = set(answers)
answer = list(temporary)

answer.sort()
if 0 in answer:
    answer.remove(0)

for i in range(len(answer)):
        print(answer[i], end = " ")
