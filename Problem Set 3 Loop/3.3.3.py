n = int(input())

for i in range(n):
   if i%2==0:
         if(i+1 == n or i+1 ==n-1):
            print(i+1, end='')
         else:
             print(i+1, '+ ', end='')
       
