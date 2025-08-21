print(" program to implement continue, break and pass statement ")

for i in range(1,7):
    if(i==5):
        continue
    print(i,end=" ")
print()

for i in range(1,8):
    if(i==5):
        break
    print(i,end=" ")
print()

for i in range(1,7):
    if i==4 :
        pass
    else:
        print(i,end=" ")  
