from art import calculator
print(calculator)
# add
def add(n1, n2):
    return n1 + n2


# sbtract
def sbtract(n1, n2):
    return n1 - n2


# mutiply
def mutiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sbtract,
    "*": mutiply,
    "/": divide
}


def calculator():
    n1 = float(input("what is the first number: \n"))
    for i in operations:
        print(i)
    Continue = True
    while Continue:
        symbol = input("choose the oporation u wanna preform: \n")
        n2 = float(input("what is the next number: \n"))
        calc = operations[symbol]
        answer = calc(n1, n2)
        print(f"{answer} {symbol} {n2} = {answer}")
        if input(f"write 'y' if u want to continue with the {answer} if not write 'n': \n") == "y":
            n1 = answer
        else:
            Continue = False
            calculator()


calculator()


