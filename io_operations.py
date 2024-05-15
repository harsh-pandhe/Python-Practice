# str = input("Enter a string: ")
# print("The string is: ", str)

f = open("test.txt", "r")
if f:
    print("File opened successfully")
    print("The file content is: ")
    print(f.read())
    f.close()

f = open("test.txt", "r")
if f:
    print("File opened successfully")
    print("The file content is: ")
    print(f.read(4))
    f.close()

f = open("test.txt", "r")
if f:
    print("File opened successfully")
    print("The file content is: ")
    print(f.readline())
    print(f.readline())
    f.close()

f = open("test.txt", "r")
if f:
    print("File opened successfully")
    print("The file content is: ")
    for a in f:
        print(a, end="")

f = open("test.txt", "r")
if f:
    print("File opened successfully")
    print("The file content is: ")
    print(f.readlines())
    f.close()

f = open("text.txt", "a")
if f:
    print("File opened successfully")
    f.write("This is the appended line")
    f = open("test.txt", "r")
    print(f.read())
    f.close()

import os

# os.rename("test.txt", "test1.txt")

try:
    print("Tried")
except:
    print("Exception")

try:
    # print(k)
    print("Tried")
except NameError:
    print("NameError")
except:
    print("Exception")


