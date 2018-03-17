#IMI

n = eval(input())

sum = 0
for i in range(n):
    if i == n-1:
        sum += (i+1)
        #print(i+1)
    else:
        sum += (i+1)
        #print(i+1, '+ ', end = '')

print("Summation of %d : %d" % (n, sum))
