list = [int(x) for x in input().split()]

while list != [1,2,3,4,5]:
    for i in range(4):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            print(str(list[0]) + " " + str(list[1]) + " " + str(list[2]) + " " + str(list[3]) + " " + str(list[4]) + " ")
