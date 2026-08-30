#  Write a program to calculate the factorial of a given number using for loop.

num = int(input('Enter a number :- '))
multi = 1

for i in range( num , 1 , -1):
    multi = multi * i

print(multi)