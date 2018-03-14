N=int(input("Enter value of N: "))
summation=0
for i in range(N):
    if((i+1)%2==0):
        summation=summation+(i+1)
    i=i+1

print(summation)

