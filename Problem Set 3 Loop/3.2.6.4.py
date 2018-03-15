n = int(input())

if(n%2==0):
    n= n-1
    
for n in range(n, 0, -2):
    for i in range(n):
        print('*', end='')
    print()

    
