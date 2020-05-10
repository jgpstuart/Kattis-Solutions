fullName = input()
abrev = ''
abrev += fullName[0]
for i in range(len(fullName)):
    if fullName[i] == '-':
        abrev += fullName[i + 1]
print(abrev)
