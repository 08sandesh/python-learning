#  Generate the fibonacci series up to n terms

n = int(input("Enter the nth term : "))

first = 0
second = 1

if n == 1:
    print(first)
else:
    print(first)
    print(second)
    for i in range(2,n):
        next = first + second
        first = second
        second = next
        print(next)