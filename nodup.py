line = [x for x in input().split()]
answer = 0
for i in range(len(line)):
    if line.count(line[i]) == 1:
        continue
    else:
        answer = 1

if answer == 0:
    print("yes")
else:
    print("no")
