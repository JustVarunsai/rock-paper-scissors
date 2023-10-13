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


games_list = [rock, paper, scissors]
choice = int(
    input(
        "WHAT YOU WANT TO CHOOSE \nType 0 for rock ,1 for paper,2 for scissors\n"
    ))
if choice >= 3 or choice < 0:
  print("Invalid Selection")
else:
  print(games_list[choice])
  choice_random = random.randint(0, 2)
  print(choice_random)
  print(games_list[choice_random])

  if choice == 0 and choice_random == 2:
    print("You Won ")
  elif choice == 2 and choice_random == 0:
    print("You Loss")
  elif choice > choice_random:
    print("You Won")
  elif choice < choice_random:
    print("You Loss")
  elif choice == choice_random:
    print("It's draw")