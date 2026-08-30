f = open("File.txt")

# lines = f.readlines()   # readlines read all lines and stores in a list
# print(lines,type(lines))

# line1 = f.readline()    # readline reads only one line
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()    # Nothing is printed
# print(line3 == "")


line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()