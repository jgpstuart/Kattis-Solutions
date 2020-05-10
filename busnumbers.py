stops = int(input())
bus = [int(x) for x in input().split()]
answer = []
bus.sort()
z=0
i=0

while i < len(bus):
    if i+1 == len(bus):
        compare = bus[i]
    else:
        compare = bus[i+1]
    if bus[i]+1 == compare:
        z += 1
    if bus[i]+1 != compare:
        if z == 0:
            answer.append(str(bus[i]))
        if z == 1:
            answer.append(str(bus[i-1]))
            answer.append(str(bus[i]))
        if z > 1:
            answer.append(str(bus[i-z]) + "-" + str(bus[i]))
        z = 0
    i += 1

for j in range(len(answer)):
    print(answer[j], end=" ")