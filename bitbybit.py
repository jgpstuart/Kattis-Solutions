length = int(input())
checklist = [2] * 32
str_answer = ""
while length != 0:
    for i in range(length):
        instruction, place, *queue = input().split()
        place = int(place)
        if len(queue) != 0:
            secondplace = int(queue[0])
        if instruction == "CLEAR":
            checklist[place] = 0
        elif instruction == "SET":
            checklist[place] = 1
        elif instruction == "OR":
            if checklist[place] == 2 and checklist[secondplace] == 2:
                checklist[place] = 2
            elif checklist[place] == 1 or checklist[secondplace] == 1:
                checklist[place] = 1
            elif checklist[place] == 2 and checklist[secondplace] == 0 or checklist[place] == 0 and checklist[secondplace] == 2:
                checklist[place] = 2
            elif checklist[place] == 0 and checklist[secondplace] == 0:
                checklist[place] = 0
        elif instruction == "AND":
            if checklist[place] == 2 and checklist[secondplace] == 0 or checklist[place] == 0 and checklist[secondplace] == 2:
                checklist[place] = 0
            elif checklist[place] == 2 or checklist[secondplace] == 2:
                checklist[place] = 2
            elif checklist[place] == 1 and checklist[secondplace] == 1:
                checklist[place] = 1
            else:
                checklist[place] = 0

    answer = []
    for i in range(len(checklist)-1, -1, -1):
        if checklist[i] == 2:
            answer.append("?")
        elif checklist[i] == 1:
            answer.append("1")
        else:
            answer.append("0")

    for i in range(len(answer)):
        str_answer += str(answer[i])

    print(str_answer)
    str_answer = ""
    checklist = [2] * 32
    length = int(input())
