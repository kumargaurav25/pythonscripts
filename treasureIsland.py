print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************

''')

print("Welcome to treasure Island")

firstdecision=input("choose left or right \n")
print("you chose "+firstdecision)
if firstdecision == "right":
    print("You made the right choice. Go On/n")
    seconddecision=input("You have come to a lake and must reach the island by waiting for boat or swim. Choose wait or swim \n")
    print("you chose "+seconddecision)
    if seconddecision == "wait":
        print ("Congratulations you chose wisely")
        thirddecision=input("final decision. 3 doors in the island. Choose left , middle or right")
        print("You chose "+thirddecision)
        if thirddecision =="left":
            print("You reached the treasure box. You WIN")
        else:
            print("oops. Dead end")
    else:
        print("Oops! the crocodiles in the water ate you")
else:
    print("you fell into a well and died")




