from sys import stdin

dictionary = {}

temp = [x for x in input().split()]

while len(temp) != 0:
    dictionary[temp[1]] = temp[0]
    temp = [x for x in input().split()]

for line in stdin:
    line = line.strip()
    print(dictionary.get(line, "eh"))
        
