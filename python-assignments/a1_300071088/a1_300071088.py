import math
import turtle


def f_to_k(t):
    """
    (number)-> number
    Takes an number t in degrees fahrenheit, returns the int in degrees kelvin
    """
    k = 5 / 9 * (t - 32) + 273  # fahrenheit to kelvin formula
    print(k)
    return


def poem_generator():
    """
    ()-> none
    Takes 2 str inputs, name and city, and concatenates them to return a poem
    """
    print("Please enter your name and city of birth.")
    x = input("Name:")
    y = input("City:")
    print(
        y + " is like a jungle.\nNo, it is a jungle. \nIt's always jumping with excitement. \nBecause of the noise, " + x + " is almost deaf. \n \nAdapted from New York City, Carmelo")
    return


def impl2loz(w):
    """
    (number)-> (int, number)
    Takes number w and returns a pair of numbers following constraints
    Preconditions: non-negative input
    """
    o = (w % 1) * 16
    l = w // 1
    l = int(l)
    print((l, o))
    return


def pale(n):
    """
    (int)-> bool
    Takes a positive 4 digit int n and returns a bool value if n is/is not a pale number.
    Preconditions: Positive 4 digit int, strings are not allowed.
    """
    x = n // 100  # first 2 digits
    y = (n // 10) % 100  # middle 2 digits
    z = n % 100  # last 2 digits
    a = n % 10  # last digit

    b = ((x != 33 and y != 33) and z != 33)  # outputs true if there are no consecutive 33s
    c = (a % 4 != 0)  # outputs true if the last digit is not divisible by 4
    d = (b and c)
    print(d)
    return


def bibformat(author, title, city, publisher, year):
    """
    (str, str, str, str, str)-> none
    Re-formats str inputs: author, title, city, publisher, year into an organized bib format.
    """
    print(author + " (" + year + "). " + title + ". " + city + ": " + publisher + ".")
    return


def bibformat_display():
    """
    ()-> none
    Prompts user for str input information, then calls the bibformat function to print formatted material.
    """
    print("Please input book information for formatting.")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter year of publication: ")
    publisher = input("Enter publisher name: ")
    city = input("Enter headquarter city of the publisher: ")

    bibformat(author, title, city, publisher, year)
    return


def compound(x, y, z):
    """
    (int, int, int)-> bool
    Takes 3 integers, x y z, returns true if x is the only even number and if any pair added together is greater than 100.
    Preconditions: No branching. x, y, z are integers

    """
    a = ((x % 2 == 0 and y % 2 != 0) and z % 2 != 0)  # checks for even numbers, returns true if x is the only even number
    b = ((x + y > 100) or (y + z > 100) or (x + z > 100))  # checks if any pair adds up to greater than 100, returns true if any pair does
    c = a and b

    print(c)
    return


def funct(p):
    """
    (number)-> none
    Takes a number p and returns the solution to the given equation.
    Preconditions: p must be greater than or equal to 11
    """
    r = ((math.log10(p-10))/(math.log10(5)))**0.5
    print("The solution is ", r)
    return


def gol(n):
    """
    (number)-> int
    Takes a number n, returns the number of times n must be divided by 2 to get a number that is less than or equal to 1
    Preconditions: n must be greater than or equal to 1
    """
    x = math.ceil(math.log(n, 2))
    print(x)
    return


def draw_rocket():
    """
    () -> none
    Draws a space ship using turtle graphics.
    """
    s = turtle.Screen()
    t = turtle.Turtle()

    # move pen
    t.penup()
    t.goto(50, 0)
    t.pendown()

    # draw cockpit
    t.setheading(90)
    t.circle(100, 180)
    t.right(90)
    t.circle(300, 45)

    # move pen
    t.penup()
    t.goto(50, 0)
    t.pendown()

    # draw wing and connect
    t.right(45)
    t.circle(300, -45)
    t.left(45)
    t.forward(625)

    # move pen
    t.penup()
    t.goto(50, 0)
    t.pendown()

    # finish cockpit
    t.right(160)
    t.circle(300, -40)

    # move pen
    t.penup()
    t.goto(50, 0)
    t.pendown()

    # finish cockpit
    t.setheading(90)
    t.left(70)
    t.circle(300, 40)

    # move pen
    t.penup()
    t.goto(100, -87)
    t.pendown()

    # draw thruster
    t.setheading(270)
    t.forward(20)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(20)

    # move pen
    t.penup()
    t.goto(-200, -87)
    t.pendown()

    # draw thruster
    t.setheading(270)
    t.forward(20)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(20)

    # move pen
    t.penup()
    t.goto(-150, -87)
    t.pendown()

    # draw thruster
    t.setheading(270)
    t.forward(20)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(20)

    # hold image till click
    s.exitonclick()
    return


def cad_cashier(price, payment):  # please print when testing function
    """
    (number, number)-> number
    Takes two non-negative numbers, price and payment, and returns the change to the nearest 0 or 5 cents
    Preconditions: Non-negative inputs, payment is greater than price
    """
    x = payment - price
    y = round(x*20)/20

    return y


def min_CAD_coins(price, payment):
    """
    (number, number) -> int
    Calls the cad_cashier function to get an amount of change, then determines the smallest number of each type of coin owed to the customer.
    Preconditions: Non-negative inputs, payment is greater than price
    """
    x = cad_cashier(price, payment)
    y = x * 100
    y = int(y)  # convert to int

    t = y // 200  # toonies
    v = y % 200

    l = v // 100  # loonies
    v1 = v % 100

    q = v1 // 25  # quarters
    v2 = v1 % 25

    d = v2 // 10  # dimes
    v3 = v2 % 10

    n = v3 // 5  # nickels

    print((t, l, q, d, n))
    return

draw_rocket()