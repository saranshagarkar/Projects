import datetime
from os import system
from time import sleep

print('''
----------------------------------------------------------------------------------------------------------------------------------------------------                 
 _____                                        _                   _     ______       _       _                   ______                        _ _ 
(_____)      _                           _   (_)                 | |   / _____)     (_)     | |         _       / _____)                      (_) |
   _   ____ | |_  ____  ____ ____   ____| |_  _  ___  ____   ____| |  | /       ____ _  ____| |  _ ____| |_    | /      ___  _   _ ____   ____ _| |
  | | |  _ \|  _)/ _  )/ ___)  _ \ / _  |  _)| |/ _ \|  _ \ / _  | |  | |      / ___) |/ ___) | / ) _  )  _)   | |     / _ \| | | |  _ \ / ___) | |
 _| |_| | | | |_( (/ /| |   | | | ( ( | | |__| | |_| | | | ( ( | | |  | \_____| |   | ( (___| |< ( (/ /| |__   | \____| |_| | |_| | | | ( (___| | |
(_____)_| |_|\___)____)_|   |_| |_|\_||_|\___)_|\___/|_| |_|\_||_|_|   \______)_|   |_|\____)_| \_)____)\___)   \______)___/ \____|_| |_|\____)_|_|           
                        
                                                        By: Arkesh Choudhary , Saransh Agarkar , Vedanth T. Sreenivasan                                                         
_____________________________________________________________________________________________________________________________________________________''')
print('\n')
user_name = input('Login ID: ')
print('\n')
pass_word = input('Password: ')
print('\n')
gen_der = input('Gender (M) , (F): ')
while gen_der not in 'MmFf':
    gen_der = input("Please input gender only as M, m, F or f: ")

# def clear1():                            # Uncomment This When Using Spyder And Comment The clear() Function.
#      from IPython import get_ipython
#      get_ipython().magic('clear')

def clear():
   if gen_der == 'M' or 'm':
      X = system('clear')              # Just Change The 'Clear' To 'Cls' When Using In Windows.
   if gen_der == 'F' or 'f':
       y = system('clear')             # Just Change The 'Clear' To 'Cls' When Using In Windows.

sleep(0.5)

# clear1()

clear()

if gen_der == 'M' or gen_der == 'm':
    print('\t','\t', '\t', 'Welcome Master' , user_name)
    print('\t', 'Date And Time Of Login: ', datetime.datetime.now())
if gen_der == 'F' or gen_der == 'f':
    print('\t', '\t', '\t', 'Welcome Miss', user_name)
    print('\t', 'Date And Time Of Login: ', datetime.datetime.now())

sleep(0.5)

# clear1()

clear()

print('''
--------------------------------------------------------------------------------------------------
                                       __      __                                  
                                 |    /  `    /  `                                 
                                 |    \__,    \__,                                 
                                                                                   
                          __       ___       __        __   ___                        
                         |  \  /\   |   /\  |__)  /\  /__` |__                         
                         |__/ /~~\  |  /~~\ |__) /~~\ .__/ |___                        
                                                                                   
      __  ___      ___       __          __   __             ___  __  ___  ___  __  
     /__`  |   /\   |  |  | /__`    .   /  ` /  \ |\ | |\ | |__  /  `  |  |__  |  \ 
     .__/  |  /~~\  |  \__/ .__/    .   \__, \__/ | \| | \| |___ \__,  |  |___ |__/ 
                                                                                   
--------------------------------------------------------------------------------------------------''')

sleep(0.5)

# clear1()

clear()

print('''--------------------------------------------------------------------------------------------------
    
    
        ___                                              _                      _                    
         |  ._ _|_  _  ._ ._   _. _|_ o  _  ._   _. |   /  ._ o  _ |   _ _|_   /   _      ._   _ o |                        
        _|_ | | |_ (/_ |  | | (_|  |_ | (_) | | (_| |   \_ |  | (_ |< (/_ |_   \_ (_) |_| | | (_ | |    
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
--------------------------------------------------------------------------------------------------''')
        
def ranker():
    order = False
    while not order:
        for i in range(len(Teams) - 1):
            if Teams[i][1] < Teams[i + 1][1]:
                Teams[i], Teams[i + 1] = Teams[i + 1], Teams[i]
                break
        else:
            order = True

Teams = [['India', 228, 8, 2], ['Australia', 220, 6, 4], ['South Africa', 198, 5, 5], ['New Zealand', 232, 4, 6], ['England', 233, 6, 4], ['Pakistan', 186, 7, 3], ['Sri Lanka', 179, 5, 5], ['Bangladesh', 171, 7, 3], ['West Indies', 170, 7, 2], ['Afghanistan', 150, 4, 6]]

proceed = 'Y'

while proceed in 'Yy':
    
    ranker()

    print("Just Type '--help' To Know The Commands.")
    sleep(0.5)
    print('\n')
    if gen_der in 'Mm':
        print('Master', user_name)
    else:
        print('Miss', user_name)
        
    cmd_num = input('Awaiting Orders --> ')
    while not cmd_num in ['1', '2', '3', '4', '5', '--help']:
        cmd_num = input("Re-enter command with a designated number only. Type '--help' to know the commands: ")

    if cmd_num == '--help':
        print('\n')
        if gen_der in 'Mm':
            print("Master", user_name, "The Available Commands Are: ")
        else:
            print("Miss", user_name, "The Available Commands Are: ")
        print('''
        [1] View Teams
        [2] View Team Record
        [3] Add A Match Result   
        [4] Add A New Team Record 
        [5] View Overall Team Ranking ''')
        cmd_num = input('Awaiting Orders --> ')
        while not cmd_num in ['1', '2', '3', '4', '5', '--help']:
            cmd_num = input("Re-enter command with a designated number only. Type '--help' to know the commands: ")

    if cmd_num == '1':
         clear()
         # clear1()
         print('\n')
         print('''
                                    +-------------------+
                                    |       Teams       |
                                    +-------------------+
                                    | [A] India         |    
                                    | [B] Australia     |    
                                    | [C] South Africa  |        
                                    | [D] New Zealand   |        
                                    | [E] England       |        
                                    | [F] Pakistan      |        
                                    | [G] Sri Lanka     |        
                                    | [H] Bangladesh    |            
                                    | [I] West Indies   |            
                                    | [J] Afghanistan   | 
                                    +-------------------+ ''')

    elif cmd_num == '2':
        clear()
        # clear1()
        print('''
                 +--------------------+
                 | Team Overall Stats |
                 +--------------------+ ''')                        
        print('\n')
        team = input('Enter Team Name: ')
        for item in Teams:
            if team.lower() == item[0].lower():
                print('\n')
                print(Teams[Teams.index(item)][0], '\n', 'Wins:', Teams[Teams.index(item)][2], '\n', '\n', 'Losses:', Teams[Teams.index(item)][3], '\n', '\n', 'Rank:', Teams.index(item), '\n')
                print('\n')
                break
        else:
            print('\n')
            print("Typo Error, Or Entered Team Not In List. Please Try Again.")

    elif cmd_num == '3':
        clear()
        # clear1()
        print('''
                         +--------------------+
                         |     Match Result   |
                         +--------------------+ ''')
        loser = input('Loosing Team: ')
        for item in Teams:
            if loser.lower() == Teams[Teams.index(item)][0].lower():
                rating_loser = Teams[Teams.index(item)][1]
                Teams[Teams.index(item)][3] += 1
                break
        else:
            print("Typo Error, Or Entered Team Not In List. Please Try Again.")
            continue
        print('\n')
        winner = input('Winning Team: ')
        for item in Teams:
            if winner.lower() == Teams[Teams.index(item)][0].lower():
                Teams[Teams.index(item)][2] += 1
                Teams[Teams.index(item)][1] += 100 / (100 + Teams[Teams.index(item)][1] - rating_loser)
                break
        else:
            print("Typo Error, Or Entered Team Not In List. Please Try Again.")
            continue
        
        print('\n')
        print('Record Updated')

    elif cmd_num == '4':
        clear()
        # clear1()
        print('''
                                +--------------------+
                                |   Adding New Team  |
                                +--------------------+ ''')
        team = input('New Team Name: ')
        print('\n')
        wins = int(input('Number Of Wins: '))
        print('\n')
        losses = int(input('Number Of Loss: '))
        print('\n')

        Teams.append([team, 100, wins, losses])                    

        print('\n','Record Updated With Default Team Rating Of 100')

    elif cmd_num == '5':
        clear()
        # clear1()
        print('''
                                        +-----------------+
                                        |   Leaderboard   |                                 
                                        +-----------------+ ''')                                         ##Just Have A Looks At Ths Arkesh Cause The Indent Is Not Right For Countries Which Have Smaller Name Like India The Indent Is Not Right.

        for team in Teams:
            print('\n', Teams.index(team) + 1, '\t', team[0], '\t', team[1])

    print('\n')
    proceed = input('Return To Menu [Y]es Or [N]o: ')
    print('\n')

    if proceed in 'Yy':
        if gen_der in 'Mm':
            print('Sure, Master', user_name, '!')
        else:
            print('Sure, Miss', user_name, '!')
        sleep(0.5)
        clear()
        # clear1()
        print('''--------------------------------------------------------------------------------------------------


                    ___                                              _                      _                    
                     |  ._ _|_  _  ._ ._   _. _|_ o  _  ._   _. |   /  ._ o  _ |   _ _|_   /   _      ._   _ o |                        
                    _|_ | | |_ (/_ |  | | (_|  |_ | (_) | | (_| |   \_ |  | (_ |< (/_ |_   \_ (_) |_| | | (_ | |    


        --------------------------------------------------------------------------------------------------''')

