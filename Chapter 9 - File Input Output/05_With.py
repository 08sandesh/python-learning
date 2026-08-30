f = open("File.txt")
print(f.read())
f.close()

#  The same can be written using with statement like this :

with open("File.txt") as f:
    print(f.read())

#  You don't have to explicitly close the file