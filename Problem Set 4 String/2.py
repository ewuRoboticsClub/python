import string

c = input("Enter a character: ")

if(c.isalpha()==True):
    print(c," is an alphabet!")
elif(c.isdigit()==True):
    print(c," is a digit!")
else:
    print(c," is a special character!")
