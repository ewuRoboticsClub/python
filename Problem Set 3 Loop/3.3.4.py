#N=int(input("Enter value of N: "))
summation=0
N=101
for i in range(N):
    if((i+1)%2!=0):
        summation=summation+((i+1)**2)
    i=i+1

print(summation)

