#IMI

char = input("Enter a single character: ")

charAscii = ord(char)

if (charAscii >= 65 and charAscii <=90):
    print("Capital letter")
elif (charAscii >= 97 and charAscii <= 122):
    print("Small letter")
else:
    print("Enter correct letter for checking upper or lower case")
