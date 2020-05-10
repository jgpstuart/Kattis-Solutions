limit = int(input())
months = int(input())
dataAvailable = 0
for i in range(months):
    dataAvailable += limit
    dataAvailable -= int(input())
dataAvailable += limit
print(dataAvailable)
