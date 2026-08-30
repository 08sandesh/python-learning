a = int(input('Enter your age :- '))

# if elif else ladder

if(a >= 18):
    print('You are above 18')
    print('Thanks')
    
elif(a < 0):
    print('Please enter valid age')
    print('Thanks')

elif(a == 0):
    print('0 cannot be an age')
    print('Thanks')

else:
    print('You are below 18')
    print('Thanks')

print('End of program')