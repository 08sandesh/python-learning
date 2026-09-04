#  Find the sum of digits of a given number using a loop.

num = input("Enter a number : ")
sum = 0
for i in num:
    sum = sum + int(i)
print(sum)