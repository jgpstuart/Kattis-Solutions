test = int(input())

while test != 0:
    goal = 0
    lentest = str(test)
    for j in range(len(lentest)):
        goal += int(lentest[j])
    for i in range(10,100000):
        testgoal = 0
        for k in range(len(str(i))):
            tempvar = str(i)
            testgoal += int(tempvar[k])
        if testgoal == goal:
            print(i)
    
