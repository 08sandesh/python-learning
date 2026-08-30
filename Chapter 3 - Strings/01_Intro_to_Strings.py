a = "sandesh"
#  a = 'sandesh'
#  a = '''sandesh'''
#  a = """sandesh"""

#   0  1  2  3  4  5  6    Positive slicing
#   s  a  n  d  e  s  h
#  -7 -6 -5 -4 -3 -2 -1    Negative slicing

print(a[0])

print(a[0 : 4])   # last one is excluded 

print(a[-7 : -3])

print(a[ 0 :])   # is same as print(a[ 0 : len]) in this case len is 7
print(a[ : 4])   # is same as print(a[ 0 : 4])

print(a[0 : 4 : 2])  #  2 is step


#  [ Start : End : Step]

#  Start by default is 0
#  End by default is length of string
#  Step by default is 1

