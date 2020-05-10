tests = int(input())

for i in range(tests):
    case = input()
    if case == "P=NP":
        print("skipped")
    else:
        n1, n2 = case.split("+")
        print(int(n1) + int(n2))
