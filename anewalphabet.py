dictionary = {'a':"@", 'b':"8", 'c':"(", 'd': "|)", 'e':"3", 'f':"#", 'g':"6", 'h':"[-]",
              'i':"|", 'j':"_|", 'k':"|<", 'l':"1", 'm':"[]\/[]", 'n':"[]\[]", 'o':"0", 'p':"|D",
              'q':"(,)", 'r':"|Z", 's':"$", 't':"']['", 'u': "|_|", 'v':"\/", 'w':"\/\/", 'x':"}{",
              'y':"`/", 'z':"2"}

word = [x for x in input()]

for i in range(len(word)):
    word[i] = word[i].lower()
    if word[i] in dictionary:
        word[i] = dictionary.get(word[i])
answer = ""
for i in range(len(word)):
    answer += word[i]
print(answer)
