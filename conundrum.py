inp = input()
word = []
for i in range(len(inp)):
    word.append(inp[i])
days = 0

for i in range(0, len(word), 3):
    if word[i] != "P":
        word[i] = "P"
        days += 1
    if word[i+1] != "E":
        word[i+1] = "E"
        days += 1
    if word[i+2] != "R":
        word[i+2] = "R"
        days += 1

print(days)
