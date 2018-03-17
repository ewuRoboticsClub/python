#IMI
n = eval(input())

fac = 1
for i in range(n):
    if (i+1)==n:
        print(f"{i+1}")
        fac *= (i+1)
    else:
        print(f"{i+1}.", end="")
        fac *= (i+1)   

print("Factorial :", fac)
#print("Factorial : %d" %fac)

