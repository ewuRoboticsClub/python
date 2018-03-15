ch='y'
word=[]
while ch=='y':
    c=str(input("Enter a word: "))
    word.append(c)
    ch=str(input("Continue? (y/n)"))

word.sort()
print(word)
