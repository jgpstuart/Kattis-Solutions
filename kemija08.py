sentence = input()
answer = ""

control = 0
while control < len(sentence):
    if sentence[control] == 'a' or sentence[control] == 'e' or sentence[control] == 'i' or sentence[control] == 'o' or sentence[control] == 'u':
        answer += sentence[control]
        control += 3
    else:
        answer += sentence[control]
        control += 1

print(answer)
    
