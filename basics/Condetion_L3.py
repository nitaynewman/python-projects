# odd or even
number = int(input("Which number do you want to check? "))
if number % 2 == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")

# BMI test wuth if statments
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight / (height ** 2))
# print(BMI)

if BMI < 18.5:
    print(f"Your BMI is under {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")

# leap year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"the year {year} is a leap year")
        else:
            print(f"the year {year} is not a leap year")
    else:
        print(f"the year {year} is a leap year")
else:
    print(f"the year {year} is not a leap year")

# pizza place
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0
if size == "S":
    price += 15
    if add_pepperoni == "Y":
        price += 2
    if extra_cheese == "Y":
        price += 1
elif size == "M":
    price += 20
    if add_pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1
else:
    price += 25
    if add_pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1
print(f"Your final bill is: ${price}.")

# love calculator
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
score1 = 0
score2 = 0
names = name1.lower() + name2.lower()
T = names.count("t")
R = names.count('r')
U = names.count('u')
A = names.count('e')
score1 = (T + R + U + A) * 10
str(score1)
L = names.count("l")
O = names.count('o')
V = names.count('v')
E = names.count('e')
score2 = L + O + V + E
str(score2)
score = score1 + score2
finalScore = int(score)
if finalScore <10 or finalScore >90:
    print(f"Your score is {finalScore}, you go together like coke and mentos.")
elif 40 < finalScore and finalScore < 50:
    print(f"Your score is {finalScore}, you are alright together.")
else:
    print(f"Your score is {finalScore}.")
# choose your advencher
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
L_R = input("Youwre at a cross road. Where do you want to go? 'left' or 'right. ")
if L_R == "left":
    S_W = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' for wait for a boat. Type 'swim' to swim across. ")
    if S_W == "wait":
        R_Y_B = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Witch colour do you choose? ")
        if R_Y_B == "yellow":
            print("you win")
        else:
            print("you loose")
    else:
        print("you loose")
else:
    print("you loose")