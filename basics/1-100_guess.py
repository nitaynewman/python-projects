import random

print('welcome to the guessing game')
print('im thinking of a number between 1 and 100 \n can u guess what it is?')
number = random.randint(1, 100)

times = 0
guess = 0
i = True
while i == True:
    mode = input("easy or hard mode: ")
    if mode == "easy":
        times = 10
        i = False
    elif mode == "hard":
        times = 5
        i = False
    else:
        print(f"oops the word {mode} is not one of the options try again")

g = True
while g == True and times > 0:
    print(f"you have {times} attempts")
    guess = int(input("guess a nmber between 1 and 100: "))
    if guess > number:
        print("To high")
        times -= 1
        if times != 0:
            print("try again")
    elif guess < number:
        print("To low")
        times -= 1
        if times != 0:
            print("try again")
    elif guess == number:
        print(f"u win, the answer is {number}")
        g = False
if times == 0:
    print(f"u loose, the answer was {number}")

