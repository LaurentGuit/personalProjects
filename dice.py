import sys , random

# creating dice variable
die1 = 0
die2 = 0

# main loop for rolling dice
while True :
    print('>>> what would you like to do? \n r = roll dice , Any other key to quit')
    
    userChoice = input()
    
    # outcome for user choice
    for diceRole in range(1):
        if userChoice == 'r':
        
            die1=random.randint(1, 6)
            die2=random.randint(1, 6)
            print('your dice rolled \n'+ str(die1)+':'+str(die2)+'\n')
        
        else:
            sys.exit()
        
    