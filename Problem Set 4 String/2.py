#IMI

char = input("Enter a single character: ")

charAscii = ord(char)

if charAscii >= 33 and charAscii <= 47:
    print("Special Character")
elif charAscii >= 48 and charAscii <= 57:
    print("Digit")
elif (charAscii >= 65 and charAscii <=90) or (charAscii >= 97 and charAscii <= 122):
    print("Alphabet")
