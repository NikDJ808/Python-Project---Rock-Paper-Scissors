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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))



if user == 0:
  print(rock)
elif user == 1:
  print(paper)
elif user == 2:
  print(scissors)
else: 
  print("You've entered an unspecified value.\n")

print("Computer chose:\n")

cpu = random.randint(0,2)

if cpu == 0:
  print(rock)
elif cpu == 1:
  print(paper)
else: 
  print(scissors)


if user == cpu:
  print("It's a draw.")
elif user == 0 and cpu == 1:
  print("Computer wins.")
elif user == 0 and cpu == 2:
  print("You win!")
elif user == 1 and cpu == 0:
  print("You win!")
elif user == 1 and cpu == 2:
  print("Computer wins.")
elif user == 2 and cpu == 0:
  print("Computer wins.")
elif user == 2 and cpu == 1:
  print("You win!")
else:
  print("Unrecognized condition.")
