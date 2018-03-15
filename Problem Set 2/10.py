N=int(input("Enter A Year: "))
if((N%4==0 and N%100!=0) or (N%100==0 and N%400==0)):
    print("Leap Year!!")
else:
    print("Not a Leap Year!!!")
