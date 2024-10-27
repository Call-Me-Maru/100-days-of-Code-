from scipy.optimize import direct

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Which direction would you like to go? Left or Right?\n")
if choice1 == "left" or choice1 == "Left":

    choice2 = input("You found a river! Do you Swim or do you Wait?\n")
    if choice2 == "Wait" or choice2 == "wait":

        choice3 = input("You've found a red door, a yellow door and a blue door, which one do you choose? Red, Yellow or Blue?\n")
        if choice3 == "red" or choice3 == "Red":
            print("You fell into lava! GAME OVER")
        elif choice3 == "blue" or choice3 == "Blue":
            print("You've been locked inside with a lion! GAME OVER")
        elif choice3 == "Yellow" or choice3 == "yellow":
            print("You've found the treasure! CONGRATULATIONS! ")
        else:
            print("Not a valid input.")

    elif choice2 == "Swim" or choice2 == "swim":
        print("You were eaten by an alligator! GAME OVER")
    else:
        print("Not a valid input.")


elif choice1 == "right" or choice1 == "Right":
    print("You've been shot by an arrow! GAME OVER ")
else:
    print("Not a valid input.")
