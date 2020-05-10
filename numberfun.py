tests = int(input())

for i in range(tests):
    a, b, c = [int(x) for x in input().split()]
    if c == b + a or c == b - a or c == a - b or c == b * a or c == b / a or c == a / b:
        print("Possible")
    else:
        print("Impossible")
