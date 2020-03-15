'''
It is the multiple line comment
Here is the Map of the House                    
                                                North
Hall(Key)    Dinning Room                    West    East
Kitchen(Monster)    Bed Room                    South

Room can be expanded depends upon you. Play this short Maze game inside house and cheers!
'''

def go(l,home):
    i=0
    if(l in home):
        i=1
    else:
        print("You can't go that way")
    if(i==1):
        print("You are in the ",end="")     #end="" it the by default new line printing. Thus next print statement will print beside it.
        a=list(home.keys())
        print(a[a.index(l)])
        direct=input("\nEnter the direction: ")
        if(direct in home[l]):
            n=home[l][direct]
            print("\nYou are in the ",n)
            if 'monster' in home[n]['item']:
                print("\nGame Over! Monster caught you")
                return()
            elif 'Key' in home[n]['item']:
                print("\nYou found the key and You won")
                return()
            else:
                print("\nTo Win, Go to the another room, find Key")
        else:
            print("\nYou can't go there")
    d=input("\nWant to go elsewhere, Press Y/N: ")
    if d=='y' or d=="Y":
        go(home[l][direct],home)    #calling function again, depending upon the user input (Yes or No)
    else:
        return

#creating home with room.  To connect all the room we need to specific the connection between rooms
home={"Hall":{'south':'Kitchen','east':'Dinning Room','item':'Key'},'Kitchen':{'north':'Hall','east':'Bed Room','item':'monster'},'Dinning Room':{'west':'Hall','south':'Bed Room','item':'Health'},'Bed Room':{'north':'Dinning Room','west':'Kitchen','item':'Near Door'}}
print("\nAvailable Rooms are: ",[x for x in home])      #shows the room present in your house
go("Bed Room",home)         #starting with bed room, you also change to other room or let user decide from where to start