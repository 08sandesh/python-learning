# Write a program which finds out whether a given name is present in a list or not.

l = ['sandesh' , 'praneeth' , 'kalpesh' , 'om' , 'parth' , 'tanmay' , 'jayesh' , 'yash' , 'krushna' , 'pratham']

name = input('Enter name :- ')

if( name in l):
    print('Given name is present in list')

else:
    print('Given name is not present in list')