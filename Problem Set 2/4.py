N=float(input("Enter Number: "))
if(N>=97 and N<=100):
    print("Grade: A+")
elif(N>=90 and N<97):
    print("Grade: A")
elif(N>=87 and N<90):
    print("Grade: A-")
elif(N>=83 and N<87):
    print("Grade: B+")
elif(N>=80 and N<83):
    print("Grade: B")
elif(N>=77 and N<80):
    print("Grade: B-")
elif(N>=73 and N<77):
    print("Grade: C+")
elif(N>=70 and N<73):
    print("Grade: C")
elif(N>=67 and N<70):
    print("Grade: C-")
elif(N>=63 and N<67):
    print("Grade: D+")
elif(N>=60 and N<63):
    print("Grade: D")
elif(N>100):
    print("Error !!!")
    print("You can't get more than 100 !!")
else:
    print("Grade: F")
    print("Sorry !! You have failed the course!!")
