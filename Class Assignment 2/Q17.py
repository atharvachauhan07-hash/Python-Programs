print("program to check whether a number is prime or not")

n=int(input("Enter the number : "))

if(n<=1):
    print("Its not a prime number ")
else:
    for i in range(2,n) :
        if(n%i==0):
            print("Its not a prime number")
            break

    else:
     print("Yes its a Prime number")

