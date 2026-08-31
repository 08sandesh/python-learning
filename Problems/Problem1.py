# WAP to check whether a number is a palindrome or not.

# num = list(input("Enter a number : "))
# newli = []

# for i in num:
#     newli.append(i)

# newli.reverse()

# if num == newli:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")

#  OR

num = list(input("Enter a number : "))
new = num.copy()

num.reverse()

if num == new:
    print("Number is palindrome")
else:
    print("Number is not palindrome")