text = input()
ascore = 0
bscore = 0
finishrule = 1
winner = "none"

for i in range(0,len(text), 2):
    if text[i] == "A":
        ascore += int(text[i+1])
    else:
        bscore += int(text[i+1])
    if ascore == 10 and bscore == 10:
        finishrule = 2
    if finishrule == 1:
        if ascore == 11:
            print("A")
        elif bscore == 11:
            print("B")
    elif finishrule == 2:
        if ascore - bscore >= 2:
            print("A")
        elif bscore - ascore >= 2:
            print("B")
