import math

cases = int(input())

for i in range(cases):
    answer = ""
    phrase = input()
    square = math.ceil(math.sqrt(len(phrase)))
    while len(phrase) < (square * square):
        phrase += "*"
    for i in range(square, 0, -1):
        start = len(phrase) - i
        while start >= 0:
            if phrase[start] != "*":
                answer += phrase[start]
            start -= square
    print(answer)
            
        

