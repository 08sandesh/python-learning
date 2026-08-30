#  Write a program to find out the line number where python is present from Q6

with open("Log.txt") as f:
    count = 1
    content = f.readline()
    while "python" not in content:
        content = f.readline()
        count = count + 1
    print(f"python is present on line {count}")