# basic for loop - avrege height
'''
    1. list of students height (avrage)
    2. create list from numbers (1 2 3 4 = [1, 2, 3, 4]) and highest num
    3. sum of range of numbers
    4. game of Fizz till 100
    5. create password ganorator
'''



student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
height = 0
for h in student_heights:
  height += h
number = 0
for num in student_heights:
  number += 1

SUM = round(height / number)

# easyer way to do it #
# SUM = sum(student_heights)
# NUM = len(student_heights)
# AVREGE = SUM / NUM
print(SUM)

# min and max for loop
student_grads = input("Input a list of student scores ").split()
for n in range(0, len(student_grads)):
  student_grads[n] = int(student_grads[n])
print(student_grads)
hi = 0
for u in student_grads:
  if hi < u:
    hi = u
print(f"The highest score in the class is: {hi}")

# add all even number in range
# print("sum of all even numbers \n")
num = 0
for i in range(2, 101, 2):
    num += i
print(f"the sum of all the even numbers is {num} \n")

# FizzBuzz game
print("lets play FizzBuzz")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for l in range(1, nr_letters + 1):
  let = random.choice(letters)
  password += let
for n in range(1, nr_numbers + 1):
  num = random.choice(numbers)
  password += num
for s in range(1, nr_symbols + 1):
  sym = random.choice(symbols)
  password += sym
# print(password)
print(f"easy answer: {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_l = []
for l in range(1, nr_letters + 1):
  let = random.choice(letters)
  password_l += let
for n in range(1, nr_numbers + 1):
  num = random.choice(numbers)
  password_l += num
for s in range(1, nr_symbols + 1):
  sym = random.choice(symbols)
  password_l += sym
# print(password)
random.shuffle(password_l)
# print(password_l)

newPassword = ""
for i in password_l:
  newPassword += i
print(f"hard answer: {newPassword}")