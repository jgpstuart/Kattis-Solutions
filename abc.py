list = [int(x) for x in input().split()]

list.sort()

A = str(list[0])
B = str(list[1])
C = str(list[2])

order = input()
answer = ""

for i in range(len(order)):
    test = order[i]
    if test == "A":
        answer += A + " "
    elif test == "B":
        answer += B + " "
    else:
        answer += C + " "

print(answer)
