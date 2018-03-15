c=str(input("Enter a string: "))
U=0
L=0
for i in c:
    if(i.isupper()==True):
        U=U+1
    elif(i.islower()==True):
        L=L+1
    else:
        continue

print("Upper Case count: ",U)
print("Lower Case count: ",L)
