tests = int(input())
vowels = ['a','e','i','o','u','y']

while tests != 0:
    most_repeats = -1
    answer = ""
    for j in range(tests):
        repeats = 0
        word = input()
        for i in range(len(word)-1):
            if word[i] in vowels and word[i] == word[i+1]:
                repeats += 1
        if repeats > most_repeats:
            answer = word
            most_repeats = repeats
    print(answer)
    tests = int(input())
        