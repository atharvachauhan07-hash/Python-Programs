print("program to calculate profit or loss")

cp=int(input("Enter the Cost Price : "))
sp=int(input("Enter the Selling Price : "))

if(sp>cp):
    profit=sp-cp
    print("Its a Profit of : ",profit)
elif(cp>sp):
    Loss=cp-sp
    print("Its a Loss of : ",Loss)    
else:
    print("Its a break even")    