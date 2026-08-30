#  Label the program written in problem 4 with comments

import os  # Importing the os module to interact with the operating system

# Specify the directory path whose contents you want to print
# You can replace this with any folder path, or use "." for the current directory
path = "/"

try:
    # os.listdir(path) returns a list of all files and folders inside the given directory
    entries = os.listdir(path)

    print("Contents of directory:", path)

    # Loop through each item in the list and print it
    for name in entries:
        print(name)

except Exception as e:
    # If something goes wrong (like an invalid path), print the error
    print("Error:", e)
