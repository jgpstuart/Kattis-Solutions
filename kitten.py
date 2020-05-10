kitten = int(input())
tree = []
answer = ""

appender = [int(x) for x in input().split()]
while appender != [-1]:
    tree.append(appender)
    appender = [int(x) for x in input().split()]

for i in range(len(tree)):
    for j in range(len(tree)):
        if kitten in tree[j][1:]:
            answer += (str(kitten) + " ")
            kitten = tree[j][0]
            break
answer += (str(kitten) + " ")
            
print(answer)
