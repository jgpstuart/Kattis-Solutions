number = int(input())
binary = format(number, 'b')
reverse = int(binary)
newbin = ""
for i in range(len(binary)):
    newbin += str(reverse % 10)
    reverse = reverse // 10
print(int(newbin,2))
