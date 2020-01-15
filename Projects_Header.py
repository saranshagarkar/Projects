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

# def clear1():                            # Uncomment This When Using Spyder And Comment The clear() Function.
#      from IPython import get_ipython
#      get_ipython().magic('clear')

def clear():
   if gen_der == 'M' or 'm':
      X = system('clear')              # Just Change The 'Clear' To 'Cls' When Using In Windows.
   if gen_der == 'F' or 'f':
       y = system('clear')             # Just Change The 'Clear' To 'Cls' When Using In Windows.

sleep(1)

# clear1()

clear()

if gen_der == 'M' or gen_der == 'm':
    print('\t','\t', '\t', 'Welcome Master' , user_name)
    print('\t', 'Date And Time Of Login: ', datetime.datetime.now())
if gen_der == 'F' or gen_der == 'f':
    print('\t', '\t', '\t', 'Welcome Miss', user_name)
    print('\t', 'Date And Time Of Login: ', datetime.datetime.now())

sleep(3)

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

sleep(2)

# clear1()

clear()

print('''--------------------------------------------------------------------------------------------------
    
    
        ___                                              _                      _                    
         |  ._ _|_  _  ._ ._   _. _|_ o  _  ._   _. |   /  ._ o  _ |   _ _|_   /   _      ._   _ o |                        
        _|_ | | |_ (/_ |  | | (_|  |_ | (_) | | (_| |   \_ |  | (_ |< (/_ |_   \_ (_) |_| | | (_ | |    
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
--------------------------------------------------------------------------------------------------''')
def opening_lines():
    global b
    if gen_der == 'M' or gen_der == 'm':
        print('\n')
        print('Master', user_name)
        b = int(input('Awaiting Orders --> '))
    if gen_der == 'F' or gen_der == 'f':
        print('\n')
        print('Miss', user_name)
        b = int(input('Awaiting Orders --> '))

Teams = [['India', 100, 8, 2, 1], ['Australia', 100, 6, 4, 2], ['South Africa', 100, 5, 5, 3], ['New Zealand', 100, 4, 6, 4], ['England', 100, 6, 4, 5], ['Pakistan', 100, 7, 3, 6], ['Sri Lanka', 100, 5, 5, 7], ['Bangladesh', 100, 7, 3, 8], ['West Indies', 100, 7, 2, 9], ['Afghanistan', 100, 4, 6, 10]]

proceed = 'Y'

while proceed in 'Yy':

    if gen_der == 'M' or gen_der == 'm':
        print("Just Type '--help' To Know The Commands.")
        sleep(2)
        print('\n')
        print('Master', user_name)
        a = input('Awaiting Orders --> ')

    if gen_der == 'F' or gen_der == 'f':
        print("Just Type '--help' To Know The Commands.")
        sleep(2)
        print('\n')
        print('Miss', user_name)
        a = input('Awaiting Orders --> ')

    if a == '--help':
        if gen_der == 'M' or gen_der == 'm':
            print('\n')
            print("Master", user_name, "The Avaiable Commands Are: ")
            print('''
            [1] View Teams
            [2] View Team Record
            [3] Add A Match Result   
            [4] Add A New Team Record 
            [5] View Overall Team Ranking ''')


        if gen_der == 'F' or gen_der == 'f':
            print('\n')
            print("Miss", user_name, "The Avaiable Commands Are: ")
            print('''
            [1] View Teams
            [2] View Team Record
            [3] Add A Match Result   
            [4] Add A New Team Record 
            [5] View Overall Team Ranking ''')


    if gen_der == 'M' or gen_der == 'm':
        sleep(2)
        print('\n')
        print('Master', user_name)
        cmd_num = int(input('Awaiting Orders ---> '))
    if gen_der == 'F' or gen_der == 'f':
        sleep(2)
        print('\n')
        print('Miss', user_name)
        cmd_num = int(input('Awaiting Orders ---> '))

    while not cmd_num in [1, 2, 3, 4, 5]:
        cmd_num = int(input("Re-enter command with a designated number only: "))

    if cmd_num == 1:
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

    elif cmd_num == 2:
        clear()
        # clear1()
        print('''
                 +--------------------+
                 | Team Overall Stats |
                 +--------------------+ ''')                        
        print('\n')
        team = input('Enter Team Name: ')
        for item in Teams.keys():
            if team.lower() == item.lower():
                print('\n')
                print(item, '\n', 'Wins:', Teams[item][1], '\n', '\n', 'Losses:', Teams[item][2], '\n', '\n', 'Rank:', Teams[item][3], '\n')
                print('\n')
                break
        else:
            print('\n')
            print("Typo Error, Or Entered Team Not In List. Please Try Again.")

    elif cmd_num == 3:
        clear()
        # clear1()
        print('''
                         +--------------------+
                         |     Match Result   |
                         +--------------------+ ''')
        loser = input('Loosing Team: ')
        for item in Teams.keys():
            if loser.lower() == item.lower():
                rating_loser = Teams[item][0]
                Teams[item][2] += 1
                break
        else:
            print("Typo Error, Or Entered Team Not In List. Please Try Again.")
            continue
        print('\n')
        winner = input('Winning Team: ')
        for item in Teams.keys():
            if winner.lower() == item.lower():
                Teams[item][1] += 1
                Teams[item][0] += 100 / (100 + Teams[item][0] - rating_loser)
                break
        else:
            print("Typo Error, Or Entered Team Not In List. Please Try Again.")
            continue
            print('\n')
            print('Record Updated')

    elif cmd_num == 4:
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

        Teams[team] = [100, wins, losses, len(Teams) + 1]                       ## The new team would be assigned the last rank.

        print(team,'\n','Wins:', wins,'\n','Losses:', losses,'\n','Rank:', len(Teams) + 1)
        print('\n','Record Updated With Default Team Rating Of 100')

    elif cmd_num == 5:
        clear()
        # clear1()
        print('''
                                        +--------------------+
                                        |   Ranking System   |                                 
                                        +--------------------+ ''')                                         ##Just Have A Looks At Ths Arkesh Cause The Indent Is Not Right For Countries Which Have Smaller Name Like India The Indent Is Not Right.

        rank_ctr = 1
        while rank_ctr <= len(Teams):
            for team, team_data in Teams.items():
                if team_data[3] == rank_ctr:
                    print('\n', rank_ctr, '\t', team, '\t', Teams[team][0])
            rank_ctr += 1

    print('\n')
    proceed = input('Return To Menu [Y]es Or [Enter] No: ')
    print('\n')

    if gen_der == 'M' or gen_der == 'm':
        if proceed == 'Y' or proceed == 'y':
            print('Sure Master!', user_name)
            sleep(2)
            clear()
            # clear1()
            print('''--------------------------------------------------------------------------------------------------


                        ___                                              _                      _                    
                         |  ._ _|_  _  ._ ._   _. _|_ o  _  ._   _. |   /  ._ o  _ |   _ _|_   /   _      ._   _ o |                        
                        _|_ | | |_ (/_ |  | | (_|  |_ | (_) | | (_| |   \_ |  | (_ |< (/_ |_   \_ (_) |_| | | (_ | |    


            --------------------------------------------------------------------------------------------------''')

    if gen_der == 'F' or gen_der == 'f':
        if proceed == 'Y' or proceed == 'y':
            print('Sure Miss!', user_name)
            sleep(2)
            clear()
            # clear1()
            print('''--------------------------------------------------------------------------------------------------


                    ___                                              _                      _                    
                     |  ._ _|_  _  ._ ._   _. _|_ o  _  ._   _. |   /  ._ o  _ |   _ _|_   /   _      ._   _ o |                        
                    _|_ | | |_ (/_ |  | | (_|  |_ | (_) | | (_| |   \_ |  | (_ |< (/_ |_   \_ (_) |_| | | (_ | |    


             --------------------------------------------------------------------------------------------------''')

