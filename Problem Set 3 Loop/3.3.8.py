#IMI

n = eval(input("How many numbers you want to calculate: "))

sum = 0
for i in range(n):
    m = eval(input("Enter numbers: "))
    sum += m
        #print(i+1, '+ ', end = '')

print("Summation of %d : %d" % (n, sum))
print("Average of series %d : %.2f" % (n, sum/n))
