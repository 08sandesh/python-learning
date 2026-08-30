'''
for snake : -1
for water : 0
for gun : 1
'''
while True:
    import random
    
    print("Welcome in snake-water-gun game")
    print('')
    
    computer = random.choice([-1,0,1])
    you = input("Enter your choice (s:snake,w:water,g:gun,e:exit) : ")
    print('')
    
    youdict = {'s':-1,'w':0,'g':1,'e':2}
    revdict = {-1:'Snake',0:'Water',1:'Gun',2:'Exit'}
    
    younum = youdict[you]
    
    print("Computer choose : ",revdict[computer])
    print("You choose : ",revdict[younum])
    print('')
    
    if younum == 2:
        break
    elif computer == younum:
        print("It's a draw")
    else:
        if computer == -1 and younum == 0:
            print("You Lose") 
        elif computer == -1 and younum == 1:
            print("You Win") 
        elif computer == 0 and younum == -1:
            print("You Win") 
        elif computer == 0 and younum == 1:
            print("You Win") 
        elif computer == 1 and younum == 0:
            print("You Lose") 
        elif computer == 1 and younum == -1:
            print("You Lose") 
        else:
            print("Something went wrong")