n = int(input())

for line in range(1, n+1):
    for space in range(1, (n-line)+1):
        print(end=' ')
    k=0
    while k != (2*line-1):
        print('*', end='');
        k=k+1
    print()
    
