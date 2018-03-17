#IMI

n = eval(input())

sum=0;
for i in range(1, n+1):
    if(i==n):
        print(f"{i}^2")
        sum += pow(i, 2)
    else:
        print(f"{i}^2 + ", end='')
        sum += pow(i, 2)

print("Sum : %d" % sum)
#print("Sum :", sum)
