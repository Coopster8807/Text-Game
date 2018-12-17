from __future__ import print_function
import random

playerItems = []
enteredRooms = []
openedDoors = []

def startGame():
    playerItems = []
    enteredRooms = []
    openedDoors = []
    print('Welcome to the mysterious house thing')
    raw_input("Press enter to start the game. You are allergic to tomatoes.")
    kitchen()
    playerAlive = True

def kitchen():
    global playerItems
    global enteredRooms
    global openedDoors
    exitRoom = False
    manAlive = True
    print('You have entered the kitchen')
    print("There, you see a man you've never met hugging ya mum")
    print('There is a locked door to your left labelled "door 1" and a knife on the counter')
    while exitRoom == False or playerAlive == False:          #This loop makes the loop stop as soon as the player dies or exits the room
        userAction = raw_input('What would you like to do?: ')
        if userAction in ['Quit', 'kill thyself', 'commit rope wrap', 'commit bucket kick', 'commit death']: #Quit Function
            print('Thanks for playing, loser!')
            playerAlive = False
            break
        elif userAction in ['Kill man', 'kill man', 'murder man', 'murder dude', 'stab man']: 
            if 'knife' in playerItems:
                if manAlive == False:
                    print("It would be rude to kill the man twice. Try again!")
                else:
                    print('Bang! Pow! You killed the man. Ya mum disintegrates just like Spiderman in Infinity War')
                    print("The man is now laying on the ground dead")
                    manAlive = False
            else:
                userAction = raw_input('How would you like to kill the man? Try again!')  # displays if you don't have a knife
        elif userAction in ['pick up knife', 'grab knife', 'finesse knife']:
            playerItems.append ('knife') #adds knife to player items
            print("You picked up the knife")
        elif userAction == 'open door':
            if 'key' in playerItems:
                print('The door slowly swings open.')
            else:
                print('The door is locked')
        elif userAction == 'search man' or userAction == 'Search man':
            if manAlive == True:
                print('He smacked you in the face and called you a pervert!')
                break
            else:
                print('You found a key!')
                playerItems.append ('key')
        elif userAction in ['unlock door 1', 'open door 1']:
            if 'key' in playerItems:
                print('The door slowly swings open revealing the living room')
                livingRoom() #goes to next room
            else:
                print('The door is locked')
        else:
            print("That's not a command I recognize, Try again!")
            
def livingRoom():
    global playerItems
    global enteredRooms
    global openedDoors
    exitRoom = False
    print('You entered The living room.')
    print('There, you see a rabbid dog on a rug and a gun laying on the couch')
    if 'livingRoom' in enteredRooms:
        print('This room looks vaguely familiar')
    if 'livingRoom' not in enteredRooms:
        enteredRooms.append ('livingRoom')

    while exitRoom == False:  #while the player is still in the room, operate the following functions
        userAction = raw_input('What would you like to do? ')
        if userAction in ['pick up gun', 'finesse gun', 'grab gun']:
            playerItems.append ('gun')
            print('You picked up a gun')
            
        elif userAction in ['Quit', 'kill thyself', 'commit rope wrap', 'commit bucket kick', 'commit death']: #Quit Function
            print('Thanks for playing, loser!')
            playerAlive = False
            break
            
        elif userAction in ['pet dog', "massage dog's earlobes"]: #must happen to remain alive
            print('You pet the dog and it vanishes like Spiderman in Infinity War. As it vanishes, a key appears')
            print('You pick the key up')
            playerItems.append ('blue key')
            
        elif userAction in ['remove rug', 'look under rug', 'check under rug']:
            if 'blue key' in playerItems:
                print('You find a door under the rug')
                print('You decide to open it with the key that you found')
                attic()
            else:
                print("You can't do that!")
                
        else:
            print("That's not a command I recognize, Try again!")

def sistersroom():
    global enteredRooms
    print("You entered your sister's room")
    print("It's dark, but the closet light is on")
    exitRoom = False
    while exitRoom == False
        userAction = raw_input ("What would you like to do?")
        if userAction in ['shoot the lock']:
            if 'gun' in playerItems:
                print ("You shoot open the door, and inside you find a ladder leading up to the attic")
                exitRoom = True
                attic() 
            else:
                print("Can't do that")
        elif userAction in ['Quit', 'kill thyself', 'commit rope wrap', 'commit bucket kick', 'commit death']:
            print('Thanks for playing, loser!')
            playerAlive = False
            break        
        else:
            print('Shoot the lock')
def attic():
    global enteredRooms
    global playerItems
    global openedDoors
    exitRoom = False
    boxItems = ['pencil']
    enteredRooms.append ('attic')
    print("You entered the attic.")
    print("It's pitch black, but you feel a flashlight standing on the table. You turn it on and see a dead grandma laying behind a closed box")
    while exitRoom == False:
        userAction = raw_input('What would you like to do? ')
        if userAction in ['open a box']:
            playerItems.append('pencil')
            print ("You opened a box and found a pencil.")
        elif userAction == 'erase the grandma' and 'pencil' in playerItems:
                print ("You used the eraser on the pencil to erase the dead grandma. The floor falls out from beneath you and you land in a bedroom. ")
                openedDoors.append ('door4')
                exitRoom = True
                bedroom()
        elif userAction in ['Quit', 'kill thyself', 'commit rope wrap', 'commit bucket kick', 'commit death']:
            print('Thanks for playing, loser!')
            playerAlive = False
            break
        else:
            print('Try erasing the Grandma')

def bedroom():
    global playerItems
    global enteredRooms
    global openedDoors
    enteredRooms = []
    playerItems = []
    openedDoors = []
    enteredRooms.append ('bedroom')
    print('You have entered a bedroom')
    print('There is a Subway Sandwich laying on the bed')   
    playerAlive = True
    exitRoom = False
    while playerAlive == True:
        userAction = raw_input('What would you like to do?')
        if userAction in ['eat sandwich', 'eat', 'consume']:
            print('You choke and die on tomatoes')
            playerAlive = False
        elif userAction in ['inspect', 'inspect sandwich', 'look inside', 'look', 'open', 'open sandwich']:
            print('You find tomatoes on the sandwich.')
            playerItems.append ('tomato')
            if userAction == 'eat tomatoes':
                print('You choke and die on tomatoes')
            if 'tomato' in playerItems:
                userAction = raw_input('What would you like to do?')
                if userAction in ['throw','kick','trash','get rid']:
                    print('Your tomato hits the wall. A small section opens up.')
                    userAction = raw_input('What would you like to do?')
                    openedDoors.append ('passageway')
                    if userAction in ['stay', 'dont go','dont move']:
                        print('Your house was on fire. You didnt move quick enough. You die from smoke inhalation just like the dude in that one show your mom watches, This is Us')
                    elif userAction in ['go','go in', 'enter']:
                        enteredRooms.append ('passageway')  
                        passageway() 
                        break
        elif userAction in ['Quit', 'kill thyself', 'commit rope wrap', 'commit bucket kick', 'commit death']:
            print('Thanks for playing, loser!')
            playerAlive = False
            break
        else:
            print('Try again weird person')
            

def passageway():
    global playerItems
    global enteredRooms
    global openedDoors
    print('You entered the passageway')
    userAction = raw_input('What would you like to do?')
    if userAction == 'wake up':
        print('You woke up. good job. You arent as stupid as I thought.')
    elif userAction in ['go forward', 'go', 'forward', 'straight', 'str8']:
        print('you were hit by a spike trap and died')
    elif userAction in ['Quit', 'kill thyself', 'commit rope wrap', 'commit bucket kick', 'commit death']:
            print('Thanks for playing, loser!')
            playerAlive = False
            break
    else:
        print('Your house was on fire. You didnt move quick enough. You die from smoke inhalation just like the dude in that one show your mom watches, This is Us')
