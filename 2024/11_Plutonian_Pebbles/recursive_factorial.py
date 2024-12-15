#!/usr/bin/env python3

# Recursive Function to calculate Factorial of a number
def factorial(n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    return n * factorial(n - 1)

# Driver Code
if __name__ == "__main__":
    n = 80
    print("Factorial of", n, "is:", factorial(n))


