print("program to calculate the sum of first 50 odd and even numbers." )

n=100
sum1=0
sum2=0
for i in range(1,n+1):
    if(i%2==0):
        sum1=sum1+i
       
    else:
        sum2=sum2+i

print("Sum of Even Numbers",sum1)  
print("Sum of odd Numbers : ",sum2)

    

