import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
program_choice = random.randint(0, 2)
choices = [rock, paper, scissors]

if user_choice == program_choice:
    print(f"You chose:\n{choices[user_choice]}")
    print(f"Computer chose:\n{choices[program_choice]}")
    print("Its a draw!")
elif user_choice == 1 and program_choice == 0:
    print(f"You chose:\n{choices[user_choice]}")
    print(f"Computer chose:\n{choices[program_choice]}")
    print("You win!")
elif user_choice == 2 and program_choice == 1:
    print(f"You chose:\n{choices[user_choice]}")
    print(f"Computer chose:\n{choices[program_choice]}")
    print("You win!")
elif user_choice == 0 and program_choice == 2:
    print(f"You chose:\n{choices[user_choice]}")
    print(f"Computer chose:\n{choices[program_choice]}")
    print("You win!")
else:
    print(f"You chose:\n{choices[user_choice]}")
    print(f"Computer chose:\n{choices[program_choice]}")
    print("You lose!")
