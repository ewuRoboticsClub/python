N=int(input("Enter value of N: "))
A=[]
for i in range(N):
    if(i==0):
        a=1
        A.append(a)
        i=i+1
    elif(i==1):
        b=1
        A.append(b)
        i=i+1
    else:
        c=a+b
        A.append(c)
        a=b
        b=c
        i=i+1
        
print(A)
