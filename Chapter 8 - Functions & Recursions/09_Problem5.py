#  Write a py function to print first n lines of the following pattern.

def pattern(n):
    # i = 1
    # while i <= n:
    #     print('*' * n)
    #     n = n - 1 
    if n == 0:
        return
    print('*' * n)
    pattern(n-1)

n = int(input("Enter nth line : "))
pattern(n)