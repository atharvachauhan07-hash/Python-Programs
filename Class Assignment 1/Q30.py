print("\"Mix Pattern 2\"")
n = 5
for i in range(1,n+1):
    for j in range(1, n + 1):
        if j <= i:
            print(chr(65+i-1), end=" ")
        else:
            print("*", end=" ")
    print()