print("Program to find largest of 3 numbers :-")
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=int(input("Enter 3rd number : "))

if(a>b):
    if(a>c):
        print(a ," is maximum ")
    else:
        print(c, " is maximum ")    
else:
    if(b>c):
        print(b," is maximum ")   
    else:
        print(c," is maximum ")         