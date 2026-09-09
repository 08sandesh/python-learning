#  Remove duplicate elements from a list

lst = ['sandesh',True,1,9,6,3,90,0,56,'om',False,'om',90,3.14,3.14,True,3]
newlst = []

for i in lst:
    if i not in newlst:
        newlst.append(i)

print(newlst)