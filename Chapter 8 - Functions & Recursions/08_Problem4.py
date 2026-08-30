#  Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter nth number : "))

def sum_of_nat(n):
    if n == 1:
        return 1
    return n + sum_of_nat(n-1)

sum = sum_of_nat(n)
print(f"Sum is {sum}")
