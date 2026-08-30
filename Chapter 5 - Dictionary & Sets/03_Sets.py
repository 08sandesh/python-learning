a = {}  #  This is an empty dict.

s = set()  # Empty set

print(type(a) , type(s))

s1 = {58 , 69 , 78 , 12 , 12 ,69}    #  Unempty set
#   it does not print repeated value.

print(s1)

s2 ={'mango' , 58 , 'grapes' , True , 90 , False}

print(s2)

#  Note :- Order is not preserved in set.
#          A set uses hashing internally.
#          Hashing decides the position of each element.