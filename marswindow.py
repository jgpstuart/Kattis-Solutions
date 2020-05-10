year = int(input())

months_passed = (((year - 2018) * 12) + 8)

if (months_passed % 26) < 12:
    print("yes")
else:
    print("no")




