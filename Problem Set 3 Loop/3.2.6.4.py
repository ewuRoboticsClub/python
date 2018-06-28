def oddTriangle(n):
    for i in range(n,0,-1):
        if(i%2!=0):
            for j in range(0,i):
                print("*",end='')
            print("\n")


def main():
    n=int(input("Enter A Number: "))
    oddTriangle(n)


if __name__ == '__main__':
    main()



