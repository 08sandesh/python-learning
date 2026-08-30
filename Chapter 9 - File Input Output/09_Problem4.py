#  A file contains word "Donkey" multiple times.
#  You need to write a program which replace this word with #### by updating the same line.

d = "Donkey"

with open("Donkey.txt") as f:
    data = f.read()
    newdata = data.replace(d,"####")

with open("Donkey.txt","w") as f:
    f.write(newdata)