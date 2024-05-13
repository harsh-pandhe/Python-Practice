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