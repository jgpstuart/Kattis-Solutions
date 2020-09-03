import math

tests = int(input())

for i in range(tests):
    answer = ""
    word = input()
    wordLength = len(word)
    root = int(math.sqrt(wordLength))

    for j in range(root):
        location = root - j - 1
        while (location < wordLength):
            answer += word[location]
            location += root
    print(answer)
