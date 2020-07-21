from itertools import groupby

word, target = [x for x in input().split()]

i = 0
while i < len(list)-1:
    if word[i] == word[i+1]:
        del word[i]
        del target[i]
    else:
        i += 1


# word = [x[0] for x in groupby(word)]
word = [ord(things) - 96 for things in word]
#target = [x[0] for x in groupby(target)]
target = [ord(things) - 96 for things in target]

print(word)
print(target)