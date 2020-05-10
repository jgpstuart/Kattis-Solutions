ciphertext = input()
key = input()
message = ""

for i in range(len(ciphertext)):
    letter = ord(ciphertext[i]) - (ord(key[i]) - 65)
    if letter < 65:
        letter = 90 - (65 - letter -1)
    message += chr(letter)
    key += chr(letter)

print(message)
