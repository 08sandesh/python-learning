a = int(input('Enter your age :- '))

# if elif else ladder

#   If statement number 1

if(a > 100):
    print('Welcome')

#   End of If statement number 1

#   If statement number 2

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

#   End of If statement number 2

print('End of program')

#   If can be an independent statement
#   But elif and else cannot be an independent statement