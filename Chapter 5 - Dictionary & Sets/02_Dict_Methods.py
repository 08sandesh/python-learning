profile = {
    'name' : 'Sandesh Choudhari',
    'std' : '1st year',          
    'roll no' : '09', 
    'DOB' : '30/04/2008'
}

print(profile.items())
print(profile.keys())
print(profile.values())
profile.update({'name' : 'Sandesh Choudhary' , 'language' : 'Python'})
print(profile)
print(profile.get("name")) 

print(profile.get("name1"))  #  will return none 
# print(profile['name1'])      #  will return an error

print(len(profile))