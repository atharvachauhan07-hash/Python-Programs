print("program to check whether a year is a leap year or not.")

y = int(input("Enter the year : "))
if y%4==0 and y%100!=0:
    print("Its a Leap year")
elif y%400==0 : 
    print("Its a Leap year")
else :
    print("Its not a Leap Year")