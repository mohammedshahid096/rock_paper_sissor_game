import random
compoints=0 
plyrpoints=0
randomnum = random.randint(1,3)
if randomnum == 1:
    computer = 'r'
elif  randomnum == 2:
    computer = 'p'
elif randomnum == 3:
    computer = 's'


def  gamerun(computer,player):
    if computer == player:
        return None
    if computer == 'r':
        if player=='p':
            return False
        elif player == 's':
            return True
    
    if computer == 'p':
        if player == 'r':
            return True
        elif player== 's':
            return False
    
    if computer == 's':
        if player =='p':
            return True
        elif player =='r':
            return False


def moveahead():
    global compoints
    global plyrpoints    
    player = input("your Turn:\n Rock----> r\n Paper----> p \nsisscor----> s ? ")
    select = gamerun(computer,player)
    
    print("computer selected :"+ computer)

    print("player selected : "+player)
    print("=================================")
    if(select):
        print("computer won this game")
        compoints = compoints+1
    elif(select==None):
        print("this game is tie")
    else:
        print("you won this game")
        plyrpoints = plyrpoints+1
    print("==================================")
    print("score:\ncomputer|player")
    print(compoints,"      |",     plyrpoints)
    print("==================================")



    
print("Welcome to Rock Paper Scissor")
moveahead()
# player = input("your Turn: 1.Rock(r) 2.Paper(p) 3.sisscor(s)? ")

flag = True
while flag ==True :
    print("----------------------------------------")
    run_exit_game = input("enter here : \nContinue----> c \nExit the game----> e \n")
    print("----------------------------------------")
    if (run_exit_game=='c'):
        moveahead()
    elif(run_exit_game =='e'):
        print("thanks for playing the game")
        break 
    
