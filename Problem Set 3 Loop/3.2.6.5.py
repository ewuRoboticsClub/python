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
    n=int(input("Enter Number Of Rows: "))
    Triangle(round(n/2)+1)
    reverseTriangle(round(n/2)+1)


if __name__ == '__main__':
    main()



