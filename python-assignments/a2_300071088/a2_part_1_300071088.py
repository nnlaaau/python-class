import random
import math


def elementary_school_quiz(flag, n):
    """
    (int, int)-> int
    Takes int input for type of question, flag, and number of questions, n. Depending on type and amount, the function asks the user math questions and returns the number of correct answers.
    Preconditions: flag is 0 or 1, n is 1 or 2
    """
    # random 1 digit int for the math questions
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)

    if flag == 0 and n == 1:  # subtraction and 1 question
        print("Question 1:")
        x = int(input("What is the result of " + str(a) + " minus " + str(b) + "? "))
        if x == a - b:
            return 1
        else:
            return 0
    elif flag == 0 and n == 2:  # subtraction and 2 questions
        print("Question 1:")
        x = int(input("What is the result of " + str(a) + " minus " + str(b) + "? "))
        print("Question 2:")
        y = int(input("What is the result of " + str(c) + " minus " + str(d) + "? "))
        if x == a - b and y == c - d:
            return 2
        elif (x != a - b and y == c - d) or (x == a - b and y != c - d):
            return 1
        else:
            return 0
    elif flag == 1 and n == 1:  # exponentation and 1 question
        print("Question 1:")
        x = int(input("What is the result of " + str(a) + " to the power of " + str(b) + "? "))
        if x == a ** b:
            return 1
        else:
            return 0
    elif flag == 1 and n == 2:  # exponentation and 2 questions
        print("Question 1:")
        x = int(input("What is the result of " + str(a) + " to the power of " + str(b) + "? "))
        print("Question 2:")
        y = int(input("What is the result of " + str(c) + " to the power of " + str(d) + "? "))
        if x == a ** b and y == c ** d:
            return 2
        elif (x != a ** b and y == c ** d) or (x == a ** b and y != c ** d):
            return 1
        else:
            return 0


def high_school_quiz(a, b, c):
    """
    (number, number, number)-> none
    Takes 3 numbers as input and returns the roots and type of roots the inputted numbers have
    """
    if a != 0:  # all 3 numbers non zero, meaning quadratic equations, either unique, one solution, or complex roots
        d = b * b - 4 * a * c
        e = math.sqrt(abs(d))
        if b > 0 and c > 0:  # checks to use either + or - for each input
            print("The quadratic equation " + str(a) + "x^2 +" + str(b) + "x + " + str(c) + " = 0")
        elif b > 0 and c < 0:
            print("The quadratic equation " + str(a) + "x^2 +" + str(b) + "x " + str(c) + " = 0")
        else:
            print("The quadratic equation " + str(a) + "x^2 " + str(b) + "x " + str(c) + " = 0")

        if d > 0:
            print("has real and unique roots: \n", ((-b + e) / (2 * a)), " and ", ((-b - e) / (2 * a)))
        elif d == 0:
            print("has only one solution, a real root: \n", (-b / (2 * a)))
        else:
            print("has two complex roots: \n", (-b / (2 * a)), " + i", e / (2 * a), "\n", (-b / (2 * a)), "- i",
                  e / (2 * a))
    elif a == b == c == 0:  # for all 0 inputs
        print("The quadratic equation 0x + 0 = 0 \nis satisfied for all numbers x")
    elif a == 0 and b == 0 and c != 0:  # for only a c input
        if c > 0:
            print("The quadratic equation " + str(b) + "x + " + str(c) + " = 0\nis satisfied for no number x")
        else:
            print("The quadratic equation " + str(b) + "x " + str(c) + " = 0\nis satisfied for no number x")
    else:  # for only b or c input
        if c > 0:
            print("The linear equation " + str(b) + "x + " + str(c) + " = 0\n has the following solution", (-c / b))
        else:
            print("The linear equation " + str(b) + "x " + str(c) + " = 0\n has the following solution", (-c / b))


def main():
    """
    (none)-> none
    Takes user inputs and decides which test to take, and initiates the chosen functions.
    """
    print("Welcome to my math quiz generator for students.")  # intro message
    name = input("What is your name? ")
    status = input(
        "Hi " + name + ". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

    if status == '1':  # elementary student quiz
        flag = int(input(name + ", What would you like to practice? Enter\n0 for subtraction \n1 for exponentiation\n"))
        if flag == 1 or flag == 0:
            n = int(input("How many practice questions would you like to do? Enter 0, 1, or 2: "))
            if n == 1:
                print(name + ", here is your question:")
                x = elementary_school_quiz(flag, n)  # x is the counter for correct answers
                if x == 1:
                    print("Congratulations, " + name + ", you will probably get an A tomorrow.")
                else:
                    print("I think you need some practice, " + name + ".")
            elif n == 2:
                print(name + ", here are your 2 questions:")
                x = elementary_school_quiz(flag, n)
                if x == 2:
                    print("Congratulations, " + name + ", you will probably get an A tomorrow.")
                elif x == 1:
                    print("You did okay, " + name + ", but I know you can do better.")
                else:
                    print("I think you need some practice, " + name + ".")
            elif n == 0:
                print("Zero questions. OK.")
            else:
                print("Invalid choice. Only 0, 1, or 2 is accepted.")
        else:
            print("Invalid choice. Only 0, or 1 is accepted.")
    elif status == '2':  # high school student quiz
        flag = True
        while flag:
            question = input(name + ", would you like a quadratic equation solved? ")
            question = question.strip().lower()
            if question != "yes":
                flag = False
            else:
                print("Good choice!")
                a = int(input("Enter a number the coefficient a: "))
                b = int(input("Enter a number the coefficient b: "))
                c = int(input("Enter a number the coefficient c: "))
                high_school_quiz(a, b, c)

    elif status == '3':  # rejection
        print("Ah...\n" + name + ", you are not a target audience for this software.")
    else:
        print("Invalid choice. Only 1, 2, or 3 are accepted.")

    print("Good bye " + name + "!")  # ending message
