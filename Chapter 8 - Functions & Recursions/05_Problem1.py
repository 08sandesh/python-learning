#  Write a program using functions to find the greatest of three numbers.

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))

def greatest(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3
    
print(f"Greatest number is {greatest(n1,n2,n3)}")