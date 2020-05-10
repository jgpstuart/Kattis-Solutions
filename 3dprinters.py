goal = int(input())
printers = 1
statues = 0
days = 0

while printers < goal:
    printers = printers * 2
    days += 1

print(days+1)

