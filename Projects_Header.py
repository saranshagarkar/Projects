#Start 
import datetime
from os import system
from time import sleep

print('''
---------------------------------------------------------------------------------------------------                 
 _______             _______             _______   _______   ______    _______   _________  _                              
(       )|\     /|  (  ____ ) |\     /| (  ____ ) (  ___  ) (  __  \  (       )  \__   __/ ( (    /|                  
| () () |( \   / )  | (    )| | )   ( | | (    )| | (   ) | | (  \  ) | () () |     ) (    |  \  ( |                      
| || || | \ (_) /   | (____)| | (___) | | (____)| | (___) | | |   ) | | || || |     | |    |   \ | |                          
| |(_)| |  \   /    |  _____) |  ___  | |  _____) |  ___  | | |   | | | |(_)| |     | |    | (\ \) |                          
| |   | |   ) (     | (       | (   ) | | (       | (   ) | | |   ) | | |   | |     | |    | | \   |              
| )   ( |   | |     | )       | )   ( | | )       | )   ( | | (__/  ) | )   ( |  ___) (___ | )  \  |              
|/     \|   \_/     |/        | /     \| |/        |/     \ |(______/ |/     \| \_______/ |/    )_)                                                                                 
                                                                                                    
                 By: Arkesh Choudhary , Saransh Agarkar , Vedanth T. Sreenivasan                                                         
___________________________________________________________________________________________________''')

user_name = input('Login ID: ')
pass_word = input('Password: ')
gen_der = input('Gender (M) , (F): ')

def clear():
    if gen_der == 'M' or 'm':
       X = system('clear')
    if gen_der == 'F' or 'f':
        y = system('clear')

sleep(1)

clear()

if gen_der == 'M':
    print('\t','\t', '\t','Welcome Master' , user_name)
    print('\t', 'Date And Time Of Login: ', datetime.datetime.now())
if gen_der == 'm':
    print('Welcome Master' , user_name)
    print('\t', 'Date And Time Of Login: ', datetime.datetime.now())
if gen_der == 'F':
    print('\t','\t', '\t','Welcome Miss' , user_name)
    print('\t', 'Date And Time Of Login: ', datetime.datetime.now())
if gen_der == 'f':
    print('\t','\t', '\t','Welcome Miss' , user_name)
    print('\t', 'Date And Time Of Login: ', datetime.datetime.now())

sleep(3)
clear()

print('''
--------------------------------------------------------------------------------------------------
                ______     _______  _________  _______   ______    _______   _______   _______              
                (  __  \  (  ___  ) \__   __/ (  ___  ) (  ___ \  (  ___  ) (  ____ \ (  ____ \                    
                | (  \  ) | (   ) |    ) (    | (   ) | | (   ) ) | (   ) | | (    \/ | (    \/                    
                | |   ) | | (___) |    | |    | (___) | | (__/ /  | (___) | | (_____  | (__                            
                | |   | | |  ___  |    | |    |  ___  | |  __ (   |  ___  | (_____  ) |  __)                           
                | |   ) | | (   ) |    | |    | (   ) | | (  \ \  | (   ) |       ) | | (                                  
                | (__/  ) | )   ( |    | |    | )   ( | | )___) ) | )   ( | /\____) | | (____/\                            
                (______/  |/     \|    )_(    |/     \| |/ \___/  |/     \| \_______) (_______/                        
                                                                                                                                    
                                            Status : Conneted                                                                                       
--------------------------------------------------------------------------------------------------''')


sleep(2)

clear()

print('''--------------------------------------------------------------------------------------------------
                ______     _______  _________  _______   ______    _______   _______   _______              
                (  __  \  (  ___  ) \__   __/ (  ___  ) (  ___ \  (  ___  ) (  ____ \ (  ____ \                    
                | (  \  ) | (   ) |    ) (    | (   ) | | (   ) ) | (   ) | | (    \/ | (    \/                    
                | |   ) | | (___) |    | |    | (___) | | (__/ /  | (___) | | (_____  | (__                            
                | |   | | |  ___  |    | |    |  ___  | |  __ (   |  ___  | (_____  ) |  __)                           
                | |   ) | | (   ) |    | |    | (   ) | | (  \ \  | (   ) |       ) | | (                                  
                | (__/  ) | )   ( |    | |    | )   ( | | )___) ) | )   ( | /\____) | | (____/\                            
                (______/  |/     \|    )_(    |/     \| |/ \___/  |/     \| \_______) (_______/                        
            
            [A] Student_Name                                                                                        
            [B] Student_Class                                                                                   
            [C] Student_Admission_Number   
            [D] Student_Contact_Number                                                                                                                                                                                                                                                                                                                                                                                                       
--------------------------------------------------------------------------------------------------''')


if gen_der == 'M':
    print("Just Type '--help' To Know The Commands.")
    sleep(2)
    print('\n')
    print('Master', user_name)
    a = input('Awaiting Orders --> ')
if gen_der == 'm':
    print("Just Type '--help' To Know The Commands.")
    sleep(2)
    print('\n')
    print('Master', user_name)
    a = input('Awaiting Orders --> ')
if gen_der == 'F':
    print("Just Type '--help' To Know The Commands.")
    sleep(2)
    print('\n')
    print('Miss', user_name)
    a = input('Awaiting Orders --> ')
if gen_der == 'f':
    print("Just Type '--help' To Know The Commands.")
    sleep(2)
    print('\n')
    print('Miss', user_name)
    a = input('Awaiting Orders --> ')

if a == '--help':
        if gen_der == 'M':
            print("Master" , user_name, '''The Avaiable Commands Are:
              [1] Create Database
              [2] Edit Database   
              [3] Delete Database ''')
        if gen_der == 'm':
            print("Master", user_name, '''The Avaiable Commands Are:
                [1] Create Database
                [2] Edit Database   
                [3] Delete Database ''')
        if gen_der == 'F':
            print("Miss", user_name, '''The Avaiable Commands Are:
                [1] Create Database
                [2] Edit Database   
                [3] Delete Database ''')
        if gen_der == 'f':
            print("Miss", user_name, '''The Avaiable Commands Are:
                [1] Create Database
                [2] Edit Database   
                [3] Delete Database ''')

while True:
    if gen_der == 'M':
        print('Master', user_name)
        b = int(input('Awaiting Orders --> '))
    if gen_der == 'm':
        print('Master', user_name)
        b = input('Awaiting Orders --> ')
    if gen_der == 'F':
        print('Miss', user_name)
        b = input('Awaiting Orders --> ')
    if gen_der == 'f':
        print('Miss', user_name)
        b = input('Awaiting Orders --> ')

    if b == 1 :
        name = input('Name Of The Database: ')
        print('''-----------------------------------------------------------------------------------------------
             ______     _______  _________  _______   ______    _______   _______   _______                              
             (  __  \  (  ___  ) \__   __/ (  ___  ) (  ___ \  (  ___  ) (  ____ \ (  ____ \                                     
             | (  \  ) | (   ) |    ) (    | (   ) | | (   ) ) | (   ) | | (    \/ | (    \/                                     
             | |   ) | | (___) |    | |    | (___) | | (__/ /  | (___) | | (_____  | (__                                                     
             | |   | | |  ___  |    | |    |  ___  | |  __ (   |  ___  | (_____  ) |  __)                                
             | |   ) | | (   ) |    | |    | (   ) | | (  \ \  | (   ) |       ) | | (                                               
             | (__/  ) | )   ( |    | |    | )   ( | | )___) ) | )   ( | /\____) | | (____/\                                 
             (______/  |/     \|    )_(    |/     \| |/ \___/  |/     \| \_______) (_______/                                 
                                                                                                                                        
                    [A] Student_Name                                                                                            
                    [B] Student_Class                                                                                                       
                    [C] Student_Admission_Number                                                                                        
                    [D] Student_Contact_Number
                    [E]''', name )
        print('-------------------------------------------------------------------------------------------------------')
        print('\n')
    if gen_der == 'M':
        print('Master', user_name)
        c = int(input('Awaiting Orders --> '))
    if gen_der == 'm':
        print('Master', user_name)
        c = input('Awaiting Orders --> ')
    if gen_der == 'F':
        print('Miss', user_name)
        c = input('Awaiting Orders --> ')
    if gen_der == 'f':
        print('Miss', user_name)
        c = input('Awaiting Orders --> ')
    if c == 1:
        name1 = input('Name Of The Database: ')
        print('''-----------------------------------------------------------------------------------------------
                 ______     _______  _________  _______   ______    _______   _______   _______                              
                (  __  \  (  ___  ) \__   __/ (  ___  ) (  ___ \  (  ___  ) (  ____ \ (  ____ \                                     
                | (  \  ) | (   ) |    ) (    | (   ) | | (   ) ) | (   ) | | (    \/ | (    \/                                     
                | |   ) | | (___) |    | |    | (___) | | (__/ /  | (___) | | (_____  | (__                                                     
                | |   | | |  ___  |    | |    |  ___  | |  __ (   |  ___  | (_____  ) |  __)                                
                | |   ) | | (   ) |    | |    | (   ) | | (  \ \  | (   ) |       ) | | (                                               
                | (__/  ) | )   ( |    | |    | )   ( | | )___) ) | )   ( | /\____) | | (____/\                                 
                (______/  |/     \|    )_(    |/     \| |/ \___/  |/     \| \_______) (_______/                                 

                        [A] Student_Name                                                                                            
                        [B] Student_Class                                                                                                       
                        [C] Student_Admission_Number                                                                                        
                        [D] Student_Contact_Number
                        [E]''', name)
        print('\t' '\t' '\t' '[F]' , name1)
        print('-------------------------------------------------------------------------------------------------------')
    print('\n')
    if gen_der == 'M':
        print('Master', user_name)
        d = int(input('Awaiting Orders --> '))
    if gen_der == 'm':
        print('Master', user_name)
        d = input('Awaiting Orders --> ')
    if gen_der == 'F':
        print('Miss', user_name)
        d = input('Awaiting Orders --> ')
    if gen_der == 'f':
        print('Miss', user_name)
        d = input('Awaiting Orders --> ')
    if d == 1:
        name2 = input('Name Of The Database: ')
        print('''-----------------------------------------------------------------------------------------------
                     ______     _______  _________  _______   ______    _______   _______   _______                              
                    (  __  \  (  ___  ) \__   __/ (  ___  ) (  ___ \  (  ___  ) (  ____ \ (  ____ \                                     
                    | (  \  ) | (   ) |    ) (    | (   ) | | (   ) ) | (   ) | | (    \/ | (    \/                                     
                    | |   ) | | (___) |    | |    | (___) | | (__/ /  | (___) | | (_____  | (__                                                     
                    | |   | | |  ___  |    | |    |  ___  | |  __ (   |  ___  | (_____  ) |  __)                                
                    | |   ) | | (   ) |    | |    | (   ) | | (  \ \  | (   ) |       ) | | (                                               
                    | (__/  ) | )   ( |    | |    | )   ( | | )___) ) | )   ( | /\____) | | (____/\                                 
                    (______/  |/     \|    )_(    |/     \| |/ \___/  |/     \| \_______) (_______/                                 

                            [A] Student_Name                                                                                            
                            [B] Student_Class                                                                                                       
                            [C] Student_Admission_Number                                                                                        
                            [D] Student_Contact_Number
                            [E]''', name)
        print('\t' '\t' '\t' '[F]', name1)
        print('\t' '\t' '\t' '[F]', name2)
        print('-------------------------------------------------------------------------------------------------------')
        print('\n')
        if gen_der == 'M':
            print('Master', user_name)
            e = int(input('Awaiting Orders --> '))
        if gen_der == 'm':
            print('Master', user_name)
            e = input('Awaiting Orders --> ')
        if gen_der == 'F':
            print('Miss', user_name)
            e = input('Awaiting Orders --> ')
        if gen_der == 'f':
            print('Miss', user_name)
            e = input('Awaiting Orders --> ')
        if e == 1:
            name3 = input('Name Of The Database: ')
        print('''-----------------------------------------------------------------------------------------------
                         ______     _______  _________  _______   ______    _______   _______   _______                              
                        (  __  \  (  ___  ) \__   __/ (  ___  ) (  ___ \  (  ___  ) (  ____ \ (  ____ \                                     
                        | (  \  ) | (   ) |    ) (    | (   ) | | (   ) ) | (   ) | | (    \/ | (    \/                                     
                        | |   ) | | (___) |    | |    | (___) | | (__/ /  | (___) | | (_____  | (__                                                     
                        | |   | | |  ___  |    | |    |  ___  | |  __ (   |  ___  | (_____  ) |  __)                                
                        | |   ) | | (   ) |    | |    | (   ) | | (  \ \  | (   ) |       ) | | (                                               
                        | (__/  ) | )   ( |    | |    | )   ( | | )___) ) | )   ( | /\____) | | (____/\                                 
                        (______/  |/     \|    )_(    |/     \| |/ \___/  |/     \| \_______) (_______/                                 

                                [A] Student_Name                                                                                            
                                [B] Student_Class                                                                                                       
                                [C] Student_Admission_Number                                                                                        
                                [D] Student_Contact_Number
                                [E]''', name)
        print('\t' '\t' '\t' '[F]', name1)
        print('\t' '\t' '\t' '[F]', name2)
        print('\t' '\t' '\t' '[F]', name3)
        print('-------------------------------------------------------------------------------------------------------')
        print('\n')
        if gen_der == 'M':
            print('Master', user_name)
            f = int(input('Awaiting Orders --> '))
        if gen_der == 'm':
            print('Master', user_name)
            f = input('Awaiting Orders --> ')
        if gen_der == 'F':
            print('Miss', user_name)
            f = input('Awaiting Orders --> ')
        if gen_der == 'f':
            print('Miss', user_name)
            f = input('Awaiting Orders --> ')
        if f == 1:
            name4 = input('Name Of The Database: ')
            print('''-----------------------------------------------------------------------------------------------
                         ______     _______  _________  _______   ______    _______   _______   _______                              
                        (  __  \  (  ___  ) \__   __/ (  ___  ) (  ___ \  (  ___  ) (  ____ \ (  ____ \                                     
                        | (  \  ) | (   ) |    ) (    | (   ) | | (   ) ) | (   ) | | (    \/ | (    \/                                     
                        | |   ) | | (___) |    | |    | (___) | | (__/ /  | (___) | | (_____  | (__                                                     
                        | |   | | |  ___  |    | |    |  ___  | |  __ (   |  ___  | (_____  ) |  __)                                
                        | |   ) | | (   ) |    | |    | (   ) | | (  \ \  | (   ) |       ) | | (                                               
                        | (__/  ) | )   ( |    | |    | )   ( | | )___) ) | )   ( | /\____) | | (____/\                                 
                        (______/  |/     \|    )_(    |/     \| |/ \___/  |/     \| \_______) (_______/                                 

                                [A] Student_Name                                                                                            
                                [B] Student_Class                                                                                                       
                                [C] Student_Admission_Number                                                                                        
                                [D] Student_Contact_Number
                                [E]''', name)
            print('\t' '\t' '\t' '[F]', name1)
            print('\t' '\t' '\t' '[F]', name2)
            print('\t' '\t' '\t' '[F]', name3)
            print('\t' '\t' '\t' '[F]', name3)
            print('-------------------------------------------------------------------------------------------------------')
    if gen_der == 'M':
        print('Master', user_name)
        g = int(input('Awaiting Orders --> '))
    if gen_der == 'm':
        print('Master', user_name)
        g = input('Awaiting Orders --> ')
    if gen_der == 'F':
        print('Miss', user_name)
        g = input('Awaiting Orders --> ')
    if gen_der == 'f':
        print('Miss', user_name)
        g = input('Awaiting Orders --> ')
    



















