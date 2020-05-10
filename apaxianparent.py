name, parent = [x for x in input().split()]
lasttwo = name[len(name)-2:]
lastone = name[len(name)-1:]
ovowel = ["a", "i", "o", "u", "e"]

if lasttwo == "ex":
    answer = name+parent
    print(answer)
elif lastone in ovowel:
    answer = name[:len(name)-1] + "ex" + parent
    print(answer)
else:
    answer = name+"ex"+parent
    print(answer)
