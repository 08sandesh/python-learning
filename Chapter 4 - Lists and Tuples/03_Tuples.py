tuple = ()  #  Empty tuple
tuple1 = ('mango',2,'apple','banana',2,True)  #  Unempty tuple
tuple2 = ('m')  #  This is not a tuple . This is a str.
tuple3 = ('m',)  # This is a tuple with one str value
tuple4 = (1)   #  This is not a tuple . This is a int.
tuple5 = ('1',)  # This is a tuple with one int value

print(type(tuple))
print(type(tuple2))
print(type(tuple4))

print(tuple1[0])  # Tuple indexing
print(tuple1[0:3])  # Tuple slicing
print(tuple1[0][0])  # Tuple slicing