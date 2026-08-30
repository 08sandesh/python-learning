#  Write a program tp print the contents of a directory using the os module.
#  Search online for the function which does that.

import os

path = '/' 

try:
    entries = os.listdir(path)
    print("Contents of directory:", path)
    for name in entries:
        print(name)
except Exception as e:
    print("Error:", e)
