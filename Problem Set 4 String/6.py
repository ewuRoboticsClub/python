#IMI

string = input("Enter String: ")

n= 0
small, capital = 0, 0


for n in range(len(string)):
    Ascii = ord(string[n])
    if (Ascii >= 65 and Ascii <=90):
        capital +=1
    elif (Ascii >= 97 and Ascii <= 122):
        small +=1

    #n +=1

print("Capiter\tletter: %d \nSmall\tletter: %d" %(capital, small))

