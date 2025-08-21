# Program to demonstrate all operators in Python

a = 10
b = 3

print("a =", a, " b =", b)

# a) Arithmetic Operators
print("\nArithmetic Operators:")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation
print("a // b =", a // b) # Floor Division

# b) Assignment Operators
print("\nAssignment Operators:")
x = 5
print("x =", x)
x += 2
print("x += 2 ->", x)
x -= 1
print("x -= 1 ->", x)
x *= 3
print("x *= 3 ->", x)
x /= 2
print("x /= 2 ->", x)
x %= 3
print("x %= 3 ->", x)
x **= 2
print("x **= 2 ->", x)
x //= 2
print("x //= 2 ->", x)

# c) Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# d) Logical Operators
print("\nLogical Operators:")
print("a > 5 and b < 5:", a > 5 and b < 5)
print("a > 5 or b > 5:", a > 5 or b > 5)
print("not(a > 5):", not(a > 5))

# e) Bitwise Operators
print("\nBitwise Operators:")
print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT
print("a << 2 =", a << 2) # Left Shift
print("a >> 2 =", a >> 2) # Right Shift

# f) Special Operators
print("\nSpecial Operators:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 is list2:", list1 is list2)       # Identity Operator
print("list1 is list3:", list1 is list3)
print("list1 is not list2:", list1 is not list2)

print("2 in list1:", 2 in list1)               # Membership Operator
print("5 not in list1:", 5 not in list1)
