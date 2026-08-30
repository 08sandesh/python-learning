l1 = ['sandesh','praneeth',3,True,5.89,'kalpesh']
l2 = [9,6,3,8,5]

l1.append('om')
print(l1)

l2.sort()
print(l2)

l1.reverse()
print(l1)

l2.insert(2,0)    #  (index , object)
print(l2)

l1.pop(2)     #  it takes index
print(l1)

l1.remove(3)  # it takes value of list
print(l1)

#  Lists are mutable