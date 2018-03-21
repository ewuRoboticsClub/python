#IMI

string = input("Enter string: ")

reverseString = string[::-1]

if(string == reverseString):
    print("Palindrome")
else:
    print("Not Palindrome")
