testcases = int(input())

for i in range(testcases):
    cities = int(input())
    citylist = []
    for j in range(cities):
        city = input()
        if city not in citylist:
            citylist.append(city)
    print(len(citylist))
