N = int(input("Enter Value of N: "))

for i in range(N):
    if(i==N-1):
        print(N)
        i=i+1
    else:
        print(i+1,",",end='')
        i=i+1

    
