print("find the sum of digits of a given number.")

n=int(input("Enter the number: "))

sum=0
temp=n


while(temp>0):
    digit=temp%10
    sum=sum+digit
    temp=temp//10
    
print(sum)