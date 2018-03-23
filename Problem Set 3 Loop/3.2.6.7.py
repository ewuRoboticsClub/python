#IMI
n = int(input())

value = n*2-1

space = 0 
for i in range(value, 0, -2):
    for sp in range(space):
        print(end=' ')
    for star in range(i):
        print("*", end='')
    space +=1
    print()
