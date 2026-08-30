#   Write a program to fill in a letter template given below with name and date.

# Letter = '''
#         Dear <|Name|>,
#         You are selected!
#         <|Date|>
#         '''

Letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
        '''

name = input("Enter your name :- ")
date = input("Enter today's date :- ")

print(Letter.replace('<|Name|>',name).replace('<|Date|>',date))

