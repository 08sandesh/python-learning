#  Check if two strings are anagrams.

st1 = list(input("Enter first string : "))
st2 = list(input("Enter second string : "))

st1.sort()
st2.sort()

if st1 == st2:
    print("Anagrams")
else:
    print("Not Anagrams")