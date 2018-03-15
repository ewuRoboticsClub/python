n = int(input())
m = int(n)

#for i in reversed(range(n)):
#    for j in range(i+1):
#        print('*', end='')
#    print()

for n in range(n, 0, -1):
    for i in range(n):
        print('*', end='')
    print()

    
#both form are correct, you can try any of these...
