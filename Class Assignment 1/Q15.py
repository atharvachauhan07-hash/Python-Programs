print("Right Numbered pyramid pattern (Horizontal)")
n=5

for i in range(1,n+1):
     for j in range(n-i):
          print(" ",end=" ")
     for k in range(i):
          print(i,end=" ")
     print()          
    