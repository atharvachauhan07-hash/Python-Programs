print("program to print the Fibonacci sequence")

n = int(input("Enter number of terms: "))

a, b = 0, 1
count = 0

print("Fibonacci sequence:")

while count < n:
    print(a, end=" ")
    next_num = a + b
    a = b
    b = next_num
    count += 1
