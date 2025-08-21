print("\" program to check whether a person is eligible for loan or not \n if he is having salary more than 50k and 3 years of experience. \" ")

Rs=int(input("Enter the Salary : "))
exp=int(input("Enter the Experience in years"))

if(Rs>50000 and exp>3):
    print("Eligible")
else:
    print("Not Eligible ")    