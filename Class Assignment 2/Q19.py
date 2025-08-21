print("program to find a factorial of a number")

n=int(input("Enter the number : "))

if(n==0):
   print(1)

fact=1

for i in range(1,n+1):
    fact=fact*i 
    
print("Factorial is",fact)     
