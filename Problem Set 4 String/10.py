c=str(input("Enter a string: "))

rev=c[::-1]
if(c==rev):
    print(c," is a palindrome !!")
else:
    print(c," is not a palindrome !!")


'''
[::-1] <- This is extended slice syntax. It works by doing [begin:end:step]
- by leaving begin and end off and specifying a step of -1,
it reverses a string.
'''
