tests = int(input())

for i in range(tests):
    status = ""
    name, schoolstart, DOB, courses = [x for x in input().split()]
    courses = int(courses)
    schoolstart = int((schoolstart.split("/"))[0])
    DOB = int((DOB.split("/"))[0])

    if schoolstart >= 2010 or DOB >= 1991:
        status = "eligible"
    elif courses > 40:
        status = "ineligible"
    else:
        status = "coach petitions"
    print(name + " " + status)

