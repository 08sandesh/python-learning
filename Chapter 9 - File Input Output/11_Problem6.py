#  Write a program to mine a log file and find out whether it contains 'python'

with open("Log.txt") as f:
    if "python" in f.read():
        print("Yes")
    else:
        print("No")