#%%

print('Welcome')#vedanth front end belongs to you so make it beautiful, all the outputs and display presentation is also your work

d=[{'Ind':[100,1,1]},{'Aus':[100,1,1]}]#saransh enter a few more records I have set up a couple as an example

i='Y'                                  #the key is only of three characters as it is easier to access it that way while I have written the ranking code

while i in 'Yy':

      print('Select the designated number to the command','\n','1 View the record of a team','\n','2 Input a match result','\n','3 Enter a new team record','\n','4 View overall rankings')

      x=int(input('Enter the designated number to proceed'))#vedanth all this you can edit

      if x==1:

         a=input('Enter the team name')

         for i in range(len(d)):

             for j in d[i]:

                 if j==a:                         #you guys need to understand the code so pay attention to the loops and slicings or indents I have used at various place

                    print(j,'\n','Wins:',d[i][j][1],'\n','Loses:',d[i][j][2],'\n','Rank:',i+1)#vedanth another output you can edit 

      elif x==2:

           b=input('Enter the name of the winning team')#so saransh over here you will have to slice the team names to the first three characters as I mentioned earlier for the ranking

           c=input('Enter the name of the losing team') #saransh on the info list you can the team name as another detail and display it instead of what ive chosen

           for i in range(len(d)):

               for j in d[i]:                                  #rating[1}+=100/(100+rating[-1]-rating[0])

                   if j==c:                                    #example reference to how our rating basically works

                      q=d[i][j][0]                     

               for j in d[i]:      

                   if j==b:

                      d[i][j][0]=d[i][j][0]+100/(100+d[i][j][0]-q)

           print('Record updated')          

      elif x==3:

           e=input('Enter the new team name')#again saransh as I said slicing will lead to better data validation, will become more user friendly

           f=int(input('Enter the team wins'))

           g=int(input('Enter the team loses'))

           d.append({e:[100,f,g]})

           for i in range(len(d)):     #vedanth another set of outputs

               for j in d[i]:         

                   if j==e:

                      print(j,'\n','Wins:',d[i][j][1],'\n','Loses:',d[i][j][2],'\n','Rank:',i+1)

                      print('New record has been updated with default team rating of 100')

      elif x==4:

           for i in range(len(d)):

               for j in range(len(d)):

                   if d[i][str(d[i].keys())[12:15]]>d[j][str(d[j].keys())[12:15]]:

                      d[i],d[j]=d[j],d[i]          #this code is called bubble sorting I have given an example code beneath

           print('Rankings')                    #this is a set of simple yet complicated code

           for i in range(len(d)):                   #lots of slicing going on refer to the code below                  

               print(i+1,str(d[i].keys())[12:15])

      i=input('Return to menu? y/n')

 

 

 

#%%

d={'Ind':1}

x=d.keys()              #this is a small reference to the way I have sliced to help you understand

print(str(x)[12:15])

 

 

#%%

x=[23,4,5,1]

for i in range(len(x)):                #bubble sorting

    for j in range(len(x)):

        if x[i]>x[j]:

           x[i],x[j]=x[j],x[i]

print(x)          
