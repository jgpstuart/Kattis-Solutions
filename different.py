try:
    while True:
        int1, int2 = [int(x) for x in input().split()]
        answer = int1 - int2
        if answer < 0:
            answer = answer * -1
        print(answer)
except EOFError:
    pass
