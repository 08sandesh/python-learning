# Write a program to find out whether a given post is talking about 'sandesh' or not.

post = input('Enter the post :- ')

if( 'Sandesh'.lower() in post.lower()):
    print('This post is talking about sandesh')

else:
    print('This post is not talking about sandesh')
