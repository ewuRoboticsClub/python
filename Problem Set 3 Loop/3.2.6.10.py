n = int(input())
s= 1
for line in range(n):
    for j in range(line+1):
        print(s, end=' ')
        s= s+1
    print()
