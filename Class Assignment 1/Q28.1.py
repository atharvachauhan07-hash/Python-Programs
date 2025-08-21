print("Left Inverted Alphabet Pyramid (Horizontal)")
n=5

for i in range(n):
    for j in range(n-i):
        print(chr(65+n-i-1),end=" ")
    print()    