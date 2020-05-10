tests = int(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

for i in range(tests):
    phrase = []
    missing = []
    answer = "missing "
    phrase += input().lower()
    for j in range(len(alphabet)):
        if alphabet[j] not in phrase:
            missing.append(alphabet[j])
    if len(missing) == 0:
        print("pangram")
    else:
        for i in range(len(missing)):
            answer += missing[i]
        print(answer)
