print("\"Mix Pattern 1\"")
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print(i, end=" ")
        else:
            print("*", end=" ")
    print()




