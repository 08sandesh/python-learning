#  Write a py function to remove a given word from a list and strip it at the same time.

l = ['sandesh','praneeth','yash','sh']

def rem(l,word):
    new = []
    for item in l:
        if not(item == word):
            new.append(item.strip(word))
    return new

print(rem(l,'sh'))