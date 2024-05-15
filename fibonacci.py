def fibonacci(n):
    """Calculates the Fibonacci sequence up to the nth term (inclusive)."""
    if n < 0:
        return []  # Return empty list on invalid input
    a, b = 0, 1
    result = []
    for z in range(n + 1):
        result.append(a)
        a, b = b, a + b
    return result


# Get the number of terms (handle potential input errors)
while True:
    try:
        n = int(input("Enter the number of terms: "))
        if n >= 0:
            break
        print("Invalid input. Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Calculate and print the Fibonacci series
fib_series = fibonacci(n)
print("Fibonacci Series:")
print(fib_series)
