# basic function#

'''
    1. how many cans of paint do you need to paint a wall
    2. check if prime number
'''
def paint_calc(height, width, cover):
    a = round(height * width / cover + .5)
    print(f"You'll need {a} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)


# prime number?#

def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime == True:
        print("It's a prime number.")

    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
