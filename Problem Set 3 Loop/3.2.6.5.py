def reverseTriangle(n):
    for i in range(n-1,0,-1):
        for j in range(0,i):
            print("*",end='')
        print("\n")

def Triangle(n):
    for i in range(0,n+1):
        for j in range (0,i):
            print("*",end='')
        print("\n")

def main():
    n=int(input("Enter A Number: "))
    Triangle(n)
    reverseTriangle(n)


if __name__ == '__main__':
    main()



