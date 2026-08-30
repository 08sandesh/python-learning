#  Write a program to find out whether a file is identical & matches the content of another file

with open("This.txt") as f:
    content1 = f.read()
with open("This_copy.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Identical")
else:
    print("Not Identical")