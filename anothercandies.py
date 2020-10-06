tests = int(input())

for i in range(tests):
    blank = input()
    cases = int(input())
    total = 0
    for j in range(cases):
        total += int(input())
    if total % cases != 0:
        print("NO")
    else:
        print("YES")
