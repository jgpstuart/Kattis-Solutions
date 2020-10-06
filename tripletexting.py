word = input()

strlen = int(len(word)/3)

str1 = word[:strlen]
str2 = word[strlen:strlen*2]
str3 = word[strlen*2:]

if str1 == str2:
    print(str1)
elif str1 == str3:
    print(str1)
else:
    print(str2)