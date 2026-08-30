def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

n = int(input('Enter number : '))
print(f"Factorial of {n} is {fact(n)}")


# Factorial(0) = 1
# Factorial(1) = 1
# Factorial(2) = 2 x 1
# Factorial(3) = 3 x 2 x 1
# Factorial(4) = 4 x 3 x 2 x 1
# Factorial(5) = 5 x 4 x 3 x 2 x 1
# Factorial(n) = n x n-1 x n-2 x ..... 3 x 2 x 1

# Factorial(n) = n * Factorial(n-1)