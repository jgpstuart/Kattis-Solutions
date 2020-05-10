t, a, b = [int(x) for x in input().split()]
plus100 = 10**99
less100 = .1**99

try:
    while True:
        answer = (t**a -1) / (t**b -1)
        print(answer)
        t, a, b = [int(x) for x in input().split()]
except EOFError:
    pass
