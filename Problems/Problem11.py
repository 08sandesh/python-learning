#  Find the second largest element in a list.

lst = [89,45,23,111,76,87,12,0,40,110,111]

lst.sort(reverse=True)

newlst = []

for i in lst:
    if i not in newlst:
        newlst.append(i)

print(newlst[1])