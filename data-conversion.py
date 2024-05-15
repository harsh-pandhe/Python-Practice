# Printing string converting to int base 2

s = "10010"
c = int(s, 2)
print(c)

t = float(s)
print(t)

s = "4"

c = ord(s)
print("After converting character to integer: ", end="")
print(c)

c = hex(56)
print("After converting 56 to hexadecimal string: ", end="")
print(c)

c = oct(56)
print("After Converting 56 to octal string: ", end="")
print(c)

s = "geeks"

c = tuple(s)
print(c)

c = set(s)
print(c)

c = list(s)
print(c)

a = 1
b = 2

tup = (('a', 1), ('f', 2), ('g', 3))

print(tup)
print("After converting tuple to dictionary: ", end="")
print(dict(tup))

c = complex(1, 2)
print("After converting 1 and 2 to complex number: ", end="")
print(c)

c = str(a)
print("After converting integer to string: ", end="")
print(c)

# Functions

def fun():
    return 1, 2, 3, 4

print(fun())

def hello():
    print("Hello World")

hello()

def add(a, b):
    return a + b

print(add(2, 3))

def my_func(*kids):
    print("The youngest child is " + kids[2])

my_func("Emil", "Tobias", "Linus")

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function()

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):
    return 5 * x

print(my_function(3))

def myfunc():
    num = 100
    print(num)

myfunc()

x = 103

def myfunc():
    print(x)

myfunc()

def myfunc():
    global x
    x = 300

myfunc()
print(x)

import external_module

external_module.sayHello("John")

from external_module import person1
print(person1)
print(person1["name"])


import math 

print(math.pi)
print(math.sqrt(16))
print(math.pow(2, 3))
print(math.floor(2.9))
print(math.ceil(2.1))
print(math.factorial(5))
print(math.gcd(12, 14))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))
print(math.asin(1))
print(math.acos(1))
print(math.atan(1))
print(math.degrees(1))
print(math.radians(1))
print(math.log(2))
print(math.log10(2))
print(math.log2(2))
print(math.exp(2))
print(math.e)
print(math.inf)
print(math.nan)
print(math.isfinite(2))
print(math.isinf(2))
print(math.isnan(2))
print(math.trunc(2))
print(math.copysign(2, -3))
print(math.fabs(-2))

import numpy

arr = numpy.array([1, 2, 3, 4, 5])
print(arr)

arr = numpy.array((1,2,3,4,5))
print(arr)

arr = numpy.array(42)
print(arr)

arr = numpy.array([[1, 2, 3], [4, 5, 6]])
print(arr)

arr = numpy.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

print(numpy.__version__)
print(arr.size)
print(arr.shape)
print(arr.ndim)
print(type(arr))