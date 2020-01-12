print('Welcome')#vedanth front end belongs to you so make it beautiful, all the outputs and display presentation is also your work

## Guys - Apart from the variables to store the data and the improvement on the loop flow, I've changed the variable names from a,b,c,d, etc.
## to names that would be easier to understand, should we need to review the code later on, or if Laxmi ma'am wants to just glance through

Teams = {'India':[100, 0, 0, 1], 'Australia':[100, 0, 0, 2], 'South Africa':[100, 0, 0, 3], 'New Zealand':[100, 0, 0, 4], 'England':[100, 0, 0, 5], 'Pakistan':[100, 0, 0, 6], 'Sri Lanka':[100, 0, 0, 7], 'Bangladesh':[100, 0, 0, 8], 'West Indies':[100, 0, 0, 9], 'Afghanistan':[100, 0, 0, 10]}
proceed = 'Y'

while proceed in 'Yy':
    print ('Select the designated number to the command','\n','1 View the record of a team','\n','2 Input a match result','\n','3 Enter a new team record','\n','4 View overall rankings')
    cmd_num = int(input('Enter the designated number to proceed: '))#vedanth all this you can edit

    if cmd_num == 1:
        team = input('Enter the team name: ')
        for item in Teams.keys():
            if team.lower() == item.lower():
                print(item,'\n','Wins:', Teams[item][1], '\n', 'Losses:', Teams[item][2],'\n','Rank:', Teams[item][3])#vedanth another output you can edit 
                break
        else:
            print("It seems there was a typing error, or the team you've entered isn't in our list. Try again.")

    elif cmd_num == 2:
        loser = input('Enter the name of the losing team: ')
        for item in Teams.keys():
            if loser.lower() == item.lower():
                rating_loser = Teams[item][0]
                Team[item][2] += 1
                break
        else:
            print("It seems there was a typing error, or the team you've entered isn't in our list.")    
            
        winner = input('Enter the name of the winning team: ')
        for item in Teams.keys():
            if winner.lower() == item.lower():
                Team[item][1] += 1
                Teams[item][0] += 100/(100 + Teams[item][0] - rating_loser)
                break
        else:
            print("It seems there was a typing error, or the team you've entered isn't in our list.")   
        
        print('Record updated')          

    elif cmd_num == 3:
    
        team = input('Enter the new team name')
        wins = int(input('Enter the team wins'))
        losses = int(input('Enter the team loses'))
        
        Teams[team] = [100, wins, losses, len(Teams) + 1]                       ## The new team would be assigned the last rank. (This comment should be left in the final code of the project too, except this sentence in the bracket.)
        
        print(team,'\n','Wins:', wins,'\n','Loses:', losses,'\n','Rank:', len(Teams) + 1) #vedanth another set of outputs
        print('\n','New record has been updated with default team rating of 100')
    
    elif cmd_num == 4:
    
        for i in range(len(d)):
        
            for j in range(len(d)):
            
               if d[i][str(d[i].keys())[12:15]][0]>d[j][str(d[j].keys())[12:15]][0]:
            
                  d[i],d[j]=d[j],d[i]          #this code is called bubble sorting I have given an example code beneath

        print('Rankings')                    #this is a set of simple yet complicated code
        
        for i in range(len(d)):                   #lots of slicing going on refer to the code below                  
        
            print(i+1,str(d[i].keys())[12:15],d[i][str(d[i].keys())[12:15]][0])
    
    proceed = input('Return to menu? y/n: ')
