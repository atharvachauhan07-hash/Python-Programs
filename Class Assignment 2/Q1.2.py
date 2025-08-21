print("Program to find largest of 4 numbers :-")
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=int(input("Enter 3rd number : "))
d=int(input("Enter 4th number : "))

if a >= b and a >= c and a >= d:
    largest = a
elif b >= a and b >= c and b >= d:
    largest = b
elif c >= a and c >= b and c >= d:
    largest = c
else:
    largest = d

print("The largest number is:", largest)

 