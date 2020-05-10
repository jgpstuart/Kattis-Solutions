rules, iterations = [int(x) for x in input().split()]
dict = {}

for i in range(rules):
    imp = input()
    imp = imp.split()
    pair = (imp[0], imp[2])
    dict[imp[0]] = imp[2]

seed = input()
newanswer = ""
for i in range(iterations):
    for j in range(len(seed)):
        if seed[j] in dict:
            newanswer += dict[seed[j]]
        else:
            newanswer += seed[j]
    seed = newanswer
    newanswer = ""

print(seed)
