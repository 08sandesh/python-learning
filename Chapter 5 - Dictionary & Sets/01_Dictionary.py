a = {}  #  empty dict.

profile = {
    'name' : 'Sandesh Choudhari',
    'std' : '1st year',          
    'roll no' : '09', 
    'DOB' : '30/04/2008', 

    #  Note : we can not write 0 at starting of a value in int but it can be done in string.
    #         For Octal digits (0-7) we can use 0o before them.
    #         08... , 09... are only possible in strings.
}

print(profile , type(profile))
print(profile['name'])
print(profile['DOB']) 