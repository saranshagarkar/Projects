print('Welcome')#vedanth front end belongs to you so make it beautiful, all the outputs and display presentation is also your work

Teams={'India':[100, 0, 0, 1], 'Australia':[100, 0, 0, 2], 'South Africa':[100, 0, 0, 3], 'New Zealand':[100, 0, 0, 4], 'England':[100, 0, 0, 5], 'Pakistan':[100, 0, 0, 6], 'Sri Lanka':[100, 0, 0, 7], 'Bangladesh':[100, 0, 0, 8], 'West Indies':[100, 0, 0, 9], 'Afghanistan':[100, 0, 0, 10}
proceed='Y'

while proceed in 'Yy':
    print('Select the designated number to the command','\n','1 View the record of a team','\n','2 Input a match result','\n','3 Enter a new team record','\n','4 View overall rankings')
    cmd_num = int(input('Enter the designated number to proceed: '))#vedanth all this you can edit

    if cmd_num == 1:
        team = input('Enter the team name: ')
        print(j,'\n','Wins:', ,'\n','Loses:', ,'\n','Rank:',i+1)#vedanth another output you can edit 

    elif cmd_num==2:
       b=input('Enter the name of the winning team')#so saransh over here you will have to slice the team names to the first three characters as I mentioned earlier for the ranking
       c=input('Enter the name of the losing team') #saransh on the info list you can the team name as another detail and display it instead of what ive chosen
    
       for i in range(len(d)):
    
           for j in d[i]:         #rating[1}+=100/(100+rating[-1]-rating[0])
    
               if j==c:                                    #example reference to how our rating basically works
    
                  h=d[i][j][0]                     
    
       for i in range(len(d)): 
    
           for k in d[i]:
    
               if k==b:
    
                  d[i][k][0]=d[i][k][0]+100/(100+d[i][k][0]-h)
    
       print('Record updated')          
    
    elif cmd_num == 3:
    
       e=input('Enter the new team name')#again saransh as I said slicing will lead to better data validation, will become more user friendly
    
       f=int(input('Enter the team wins'))
    
       g=int(input('Enter the team loses'))
    
       d.append({e:[100,f,g]})
    
       for i in range(len(d)):     #vedanth another set of outputs
    
           for j in d[i]:
    
               if j==e:
    
                  print(j,'\n','Wins:',d[i][j][1],'\n','Loses:',d[i][j][2],'\n','Rank:',i+1)
    
                  print('New record has been updated with default team rating of 100')
    
    elif cmd_num == 4:
    
        for i in range(len(d)):
        
            for j in range(len(d)):
            
               if d[i][str(d[i].keys())[12:15]][0]>d[j][str(d[j].keys())[12:15]][0]:
            
                  d[i],d[j]=d[j],d[i]          #this code is called bubble sorting I have given an example code beneath

        print('Rankings')                    #this is a set of simple yet complicated code
        
        for i in range(len(d)):                   #lots of slicing going on refer to the code below                  
        
            print(i+1,str(d[i].keys())[12:15],d[i][str(d[i].keys())[12:15]][0])
    
    proceed = input('Return to menu? y/n: ')
