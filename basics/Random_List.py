import random

'''
    1. heads or tails
    2. find the treasure
    3. rock paper sizers
'''


#heads or tails
H_T = random.randint(0, 1)
if H_T == 1:
  print("Heads")
else:
  print("TAILS")

# random choice in a list

names_s = input('enter your names: ')
names = names_s.split(", ")
# print(names)
pays = random.choice(names)
print(pays)

# select row and column
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? 12 ")
column = int(position[0])
row = int(position[1])

sRow = map[row -1]
sRow[column -1] = "X"
print(f"{row1}\n{row2}\n{row3}")

# rock paper sizers
rock = '''
     ___________
___/         ____)_
             (______)
             (______)
_____       (_____)
      \_____(___)
'''
paper = '''
     ____________
___/         _____)___
               ________)
               _________)
_____         ________)
      \_____________)
'''
sizers = '''
     ___________
___/        _____)____
               ________)
               _________)
_____       (_____)
      \_____(___)
'''

game = [rock, paper, sizers]
choice = int(input("enter 1 for rock, 2 for paper and 3 for sizers: "))
print(game[choice - 1])
bot = random.choice(game)
print(bot)

if choice == 1 and bot == sizers:
    print("u win")
elif choice == 1 and bot == rock:
    print("draw")

elif choice == 2 and bot == rock:
    print("u win")
elif choice == 2 and bot == paper:
    print("draw")

elif choice == 3 and bot == paper:
    print("u win")
elif choice == 1 and bot == sizers:
    print("draw")
else:
    print("u loose")