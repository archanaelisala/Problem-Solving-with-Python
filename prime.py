#prime number generation
s=0
l1=int(input('enter the starting number: '))
u1=int(input('enter the ending number: '))
print("Prime numbers between",l,"and",u,"are:")
for i in range(l1,u1+1):
   if l1>1:
      for j in range(2,i):
         if i %j==0:
            break
      else:
         s=s+i
         print(i,end=' ,')
print('\nsum is',s)
      
