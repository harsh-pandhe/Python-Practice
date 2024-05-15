a = int(input("Enter the number: "))

sum = 1

if a < 0:
    print("Enter a Positive Number!!")
elif(a ==0):
    print("The factorial of 0 is 1")
else:
    for i in range(1, a +1):
        sum = sum * i
    print("Factorial of ", a, " is ", sum)