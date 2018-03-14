N=int(input("Enter value of N: "))

for i in range(N):   
    if((i+1)%2!=0):
        if((i+1)==N or (i+1)==N-1):
            print(i+1)
        else:
            print(i+1,",",end='')
            i=i+1
