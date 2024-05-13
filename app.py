"""
Variable name is also known as identifier and used to hold value.
The first character of the variable must be an alphabet or underscore ( _ ).
All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore, or digit (0-9).
Identifier name must not contain any white-space, or special character (!, @, #, %, ^, &, *).
Identifier name must not be similar to any keyword defined in the language.
Identifier names are case-sensitive. For example myname and MyName is not the same.
Examples of valid identifiers: a123, _n, n_9, etc.
Examples of invalid identifiers: 1a, n%4, n 9, etc.
"""

a = 10
name = "John"
salary = 1000.0

print(a)
print(name)
print(salary)

# Multiple Assignment

a = b = c = 1
print(a)
print(b)
print(c)

d, e, f = 1, 2, "john"
print(d)
print(e)
print(f)

# Python variable Example
# Write the variable-name on the left side of = and the value on the right side.
num = 100
str = "Hello"
print(num)
print(str)

# Plus and concatenation operation on the variables

x = 10
y = 20
print(x + y)

str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)


"""
Immutable data types in Python are:
1. Numbers
2. String
3. Tuple
Mutable data types in Python are:
1. List
2. Dictionaries
3. Sets
"""


# Numbers
# Python supports four different numerical types:
# int (signed integers)
# long (long integers, they can also be represented in octal and hexadecimal)
a = 100
print(a, " : ", type(a))

# float (floating point real values)
b = 10.53
print(b, " : ", type(b))

# complex (complex numbers)
c = 100 + 3j
print(c, " : ", type(c))

# String

str1 = "Harsh is 19 years old."
print(str1)

str2 = "He likes Butterscotch Ice-cream."
print(str1 + " " + str2)

# List
# List is an ordered sequence of some data written using square brackets ([]) and commas (,).
# List is mutable.

list1 = [10, 20, 30, 40, 50]
print(list1)

list2 = ["apple", "banana", "cherry"]
print(list2)

list3 = [10, "apple", 20, "banana"]
print(list3)

print(list3[1])
print(list3[-2])

# Tuple
"""
Tuple is another data type which is a sequence of data similar to list.
But it is immutable.
That means data in a tuple is write protected.
Data in a tuple is written using parenthesis and commas.
"""

tuple1 = (10, 20, 30, 40, 50)
print(tuple1)

tuple2 = ("apple", "banana", "cherry")
print(tuple2)

tuple3 = (10, "apple", 20, "banana")
print(tuple3)

print(tuple3[1])

# Dictionary
"""
Python Dictionary is an unordered sequence of data of key-value pair form.
It is similar to the hash table type. Dictionaries are written within curly braces in the form key: value.
"""

dict1 = {1: "John", 2: "Bob", 3: "Alice"}
print(dict1)

dict2 = {"name": "John", "age": 25}
print(dict2)

print(dict2["name"])

# Basic Operators

# Arithmetic Operators

a = 10
b = 20

print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a % b) # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division

# Comparison Operators

a = 10
b = 20

print(a == b) # Equal
print(a != b) # Not equal
print(a > b) # Greater than
print(a < b) # Less than
print(a >= b) # Greater than or equal to
print(a <= b) # Less than or equal to

# Logical Operators

a = True
b = False

print(a and b) # Logical AND
print(a or b) # Logical OR
print(not a) # Logical NOT

# Assignment Operators

a = 10
b = 20
a += b # a = a + b
print(a)

a = 10
b = 20
a -= b # a = a - b
print(a)

a = 10
b = 20
a *= b # a = a * b
print(a)

a = 10
b = 20
a /= b # a = a / b
print(a)

a = 10
b = 20
a %= b # a = a % b
print(a)

a = 10
b = 20
a **= b # a = a ** b
print(a)

a = 10
b = 20
a //= b # a = a // b
print(a)

# Bitwise Operators

a = 10
b = 20

print(a & b) # Bitwise AND

print(a | b) # Bitwise OR

print(a ^ b) # Bitwise XOR

print(~a) # Bitwise NOT

print(a << 2) # Bitwise Left Shift

print(a >> 2) # Bitwise Right Shift

# Membership Operators

a = [1, 2, 3, 4, 5]

print(1 in a) # in operator

print(1 not in a) # not in operator

# Identity Operators

a = 10
b = 10

print(a is b) # is operator

print(a is not b) # is not operator

# Control Statements

# If Statement

a = 10

if a > 0:
    print("Positive Number")

# If-else Statement

a = -10

if a > 0:
    print("Positive Number")
else:
    print("Negative Number")

# If-elif-else Statement

a = 0

if a > 0:
    print("Positive Number")
elif a < 0:
    print("Negative Number")
else:
    print("Zero")

# Examples

# Check if a number is even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")

# Print the largest number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

# Election Eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Grade Calculation
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")