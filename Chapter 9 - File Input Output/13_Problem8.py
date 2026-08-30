#  Write a program to make a copy of a text file "This.txt"

with open("This.txt") as f:
    content = f.read()
with open("This_copy.txt","w") as f:
    f.write(content)
