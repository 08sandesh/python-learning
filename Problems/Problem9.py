#  Reverse a string without using built in functions

st = input("Enter a string : ")
l = len(st)
new = ""
for i in range(l-1,-1,-1):
    new = new + st[i]

print(new)
