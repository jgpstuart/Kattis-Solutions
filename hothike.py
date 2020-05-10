hiking_days = int(input())
temp = [int(x) for x in input().split()]
hotesthike = 10000
startday = 10000

for i in range(hiking_days - 2):
    if max(temp[i], temp[i+2]) < hotesthike:
        hotesthike = max(temp[i], temp[i+2])
        startday = i+1

    
print(str(startday) + " " + str(hotesthike))
