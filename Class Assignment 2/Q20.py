print("Finding the number of digits in the Number")
n = int(input("Enter the number : "))
i=0 
while n>0 :
    n=n//10
    i=i+1
print("Number has " ,i, "digits")