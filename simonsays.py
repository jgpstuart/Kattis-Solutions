checks = int(input())
instruction = ""

for i in range(checks):
    command = [x for x in input().split()]
    if command[0] == "Simon" and command[1] == "says":
        command.pop(0)
        command.pop(0)
        for i in range(len(command)):
            instruction += command[i] + " "
        print(instruction)
        instruction = ""
    else:
        pass


