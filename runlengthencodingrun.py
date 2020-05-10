from operator import itemgetter
from itertools import groupby

test = [x for x in input().split()]
word = []

for i in range(len(test[1])):
    word.append(test[1][i])

testword = [x[0] for x in groupby(word)]
answer = ""
count = 0
letterplace = 1
indexstart = 0

if test[0] == "E":
    for i in range(len(testword)):
        letter_test = testword[i]
        for j in range(indexstart, len(word)):
            if word[j] == letter_test:
                indexstart += 1
                count += 1
            if word[j] != letter_test or j == len(word)-1:
                answer += testword[i]
                answer += str(count)
                count = 0
                break
if test[0] == "D":
    for i in range(len(testword)):
        letter_add = word[i * 2]
        for j in range(0, int(word[letterplace])):
            answer += letter_add
        letterplace += 2
        if letterplace >= len(word):
            break
            
                       
print(answer)
