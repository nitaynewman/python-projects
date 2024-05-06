#terning int 2 str
'''
    1. amount of letters in a string
    2. adding num in string
    3. calc bmi
    4. calc num of days weeks and months befor u  die
    5. tip calc
'''




num = len(input("what is your name "))
print("your name has " + str(num) + " letters")
#finding the type of the var
print(type(num))

#convert number to the sum of its parts
number = input("Type a two digit number: ")
str(number)
print(int(number[0]) + int(number[-1]))

# BMI Calculator and terning it in to an int
height = input('enter your height in m: ')
weight = input("enter your weight in kg: ")
Bmi = int(weight) / float(height) ** 2
BMI = int(Bmi)
print(Bmi)
print(BMI)

# f-string (using difrent types of var in string)
age = input("What is your current age? ")
days = int(90 * 365 - int(age) * 365)
weeks = int(90 * 52 - int(age) * 52)
months = int(90 * 12 - int(age) * 12)
print(f"You have {days} days, {weeks} weeks and {months} months left.")

# tip calculater
print("Welcome to the tip calculator.")
total = float(input('What was the total bill? '))
percent = int(input("What percentage tip would you like to give? 10, 12, 15 "))
split = int(input("How many people to split the bill? "))
# percent = float(percent)
# total = float(total)
# split = float(split)
calck = (total * (percent / 100) + total) / split
calck = round(calck, 2)
print(f"Each person should pay: {calck}")
