N=int(input("Enter value of N: "))
number=[]

for i in range(N):
    number.append(int(input()))

number.sort()
print("Ascending Sorted: ",number)
