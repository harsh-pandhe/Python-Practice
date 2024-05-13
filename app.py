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
