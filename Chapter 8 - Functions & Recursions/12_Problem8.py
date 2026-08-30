#  Write a py fun to print multiplication table of a given number.

def tab(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter number : "))
tab(n)