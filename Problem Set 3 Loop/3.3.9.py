course=int(input("How Many Course? : "))
s=0
t=0
for i in range(course):
    print("Credit for course ",i+1," :")
    c=int(input())
    t=t+c
    print("Grade point for course ",i+1," :")
    g=float(input())
    s=s+(c*g)
    i=i+1

print("CGPA: ",s/t)
    
            
