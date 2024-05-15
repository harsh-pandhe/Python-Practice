# Loops

# for loop
for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)


# Tables

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Pattern

rows = 5 # int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(i + 1):
        print("*", end="")
    print()

# while loop
i = 0
while i < 5:
    print(i)
    i += 1

# break statement

for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement

for i in range(10):
    if i == 5:
        continue
    print(i)

# pass statement

for i in range(10):
    if i == 6:
        print("Before Pass")
        pass
        print("After Pass")
    print(i)

a = 2
for v in range(1, 6, 2):
    for q in range(v):
        print(a, end=" ")
        a += 2
    print()
