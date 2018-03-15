n = int(input())

secNd = n-1
#1st part //increasing
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()

#2nd part //decreasing

for secNd in range(secNd, 0, -1):
    for j in range(secNd):
      print('*', end='')
      
    print()

    
