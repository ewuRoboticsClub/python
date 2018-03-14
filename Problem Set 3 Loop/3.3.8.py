N=int(input("Enter value of N: "))
summation=0
for i in range(N):
    a=int(input("Give value: "))
    summation=summation+a
    i=i+1

print("Avg: ",summation/N)
