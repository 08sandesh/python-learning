#  Write a program to read the text from a given file 'Poem.txt' and 
#  find out whether it containes the word twinkle

f = open("Poem.txt")
data = f.read()
print(data)

if "twinkle" in data:
    print("Yes")
else:
    print("No")
    
f.close()