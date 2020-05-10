word = input()
answer = "no hiss"
for i in range(1, len(word)):
    if answer != "hiss":
        if word[i] == "s" and word[i-1] == "s":
            answer = "hiss"
            break
        else:
            answer = "no hiss"
print(answer)
