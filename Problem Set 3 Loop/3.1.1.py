n = int(input())
i = 3
for i in range(n):
    if i == n-1:
        print(i+1, end = '')
    else:
        print(i+1, ', ', end = '')
