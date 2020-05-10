from itertools import groupby

word, target = [x for x in input().split()]

word = [x[0] for x in groupby(word)]
word = [ord(things) - 96 for things in word]
target = [x[0] for x in groupby(target)]
target = [ord(things) - 96 for things in target]

change = 0

for i in range(len(word)):
    change += abs(word[i] - target[i])

print(change)