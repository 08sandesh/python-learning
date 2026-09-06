#  Count the number of vowels and consonants in a string.

st = input("Enter a string : ")

count = 0

for i in st:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        count = count + 1

print("Vowels in string : ",count)
print("Consonants in string : ",len(st)-count)