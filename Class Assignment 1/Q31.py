print("\"Mix Pattern 3\"")
n = 5
for i in range(1,n+1):
    for j in range(1, n + 2):
        if j <= i:
            print(chr(65+i-1), end=" ")
        else:
            print(i, end=" ")
    print()