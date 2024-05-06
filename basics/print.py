# basic printing
print(
'''Day 1 - Python Print Function
The function is declared like this:
print('what to print')''')

print("Day 1 - String Manipulation")
print("String Concatenation is done with the " + '"+"' + " sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# inputing in the midle of printing
print("your name is - " + input("what is your name? "))
# length of the string
print(len(input("what is your name? ")))
# a bit of playing with variable
a = input("a: ")
b = input("b: ")
print("a: " + a)
print("b: " + b)
# entering to variabales and printing them
print("Welcome to the Band Name Generator.")
city_name = input("What's name of the city ou grew up in? \n")
pet_name = input("What's your pet's name? \n")
print("Your band name could be " + city_name + " " + pet_name)
