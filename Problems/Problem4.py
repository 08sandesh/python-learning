#  Print all prime numbers between 1 to 100.

# for i in range(2,101):
#     count = 0
#     for j in range(1,i+1):
#         if i%j == 0:
#             count = count + 1
#     if count == 2:
#         print(i,end="\n")

#  OR

for i in range(2,101):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)