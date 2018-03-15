N=float(input("Enter Age: "))
R=str(input("Have you registered yourself as voter? (y/n) :"))
if(N<18 or R=="n"):
    print("You are not a voter yet!!")
else:
    print("congratulation!! you are a voter!!")
