adventures = int(input())

for i in range(adventures):
    backpack = []
    journey = list(input())
    answerprinted = False
    for j in range(len(journey)):
        if journey[j] == '.':
            continue
        elif journey[j] == "$":
            backpack.append("$")
        elif journey[j] == '|':
            backpack.append('|')
        elif journey[j] == '*':
            backpack.append('*')
        elif journey[j] == 't':
            if len(backpack) > 0:
                if backpack[len(backpack)-1] == '|':
                    backpack.pop()
            else:
                print("NO")
                answerprinted = True
                break
        elif journey[j] == 'j':
            if len(backpack) > 0:
                if backpack[len(backpack)-1] == '*':
                    backpack.pop()
            else:
                print("NO")
                answerprinted = True
                break
        elif journey[j] == 'b':
            if len(backpack) > 0:
                if backpack[len(backpack)-1] == '$':
                    backpack.pop()
            else:
                print("NO")
                answerprinted = True
                break
    if answerprinted == False:
        if j + 1 == len(journey):
            if len(backpack) == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
