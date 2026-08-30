s1 = {True , 43 , 'Earth' , 98 , False}

s2 = {23 , 'Moon' , 'Sun' , 56 , 98 , True}

print(s1.union(s2))
print(s1.intersection(s2))

print(s1 - s2)
print(s2 - s1)
# print(s2 + s1)  '+' is not supported

print({True , False}.issubset(s1))

a={1,2,5,6,8}
b={3,1,4,7}
print(a.difference(b))
