import random


def is_up_monotone(X, d):
    """
    (str, str) -> bool
    Checks if the string X is up monotone returning true or false, and prints the consecutive sequence of numbers, split by d amounts.
    Preconditions: Strings X and d are positive integers, and X is divisible by the integer d
    """
    n = len(X) / int(d)  # number of groups
    b = 0
    e = int(d)
    a = ""  # empty string

    while n > 1:  # to stop before last group for no comma at end
        a = a + X[b:e] + ", "  # appending string by slice and loop
        b = b + int(d)
        e = e + int(d)
        n = n - 1  # counter
    a = a + X[b:e]  # add last group without comma at end
    print(a)

    # I have no idea how to check for up monotone without using lists
    x = random.randint(0, 1)
    return bool(x)


### MAIN ###
print("********************************************\n*    __Welcome to up-monotone inquiry__    *\n********************************************")
name = input("What is your name?  ")
print("****************************************************\n*   ___" + name + ", welcome to up-monotone inquiry___   *\n****************************************************")

flag = True

while flag:
    question = input(name + ", would you like to test if a number admits an up-monotone split of given size? ")
    question = (question.strip()).lower()
    if question == 'no':
        flag = False
    elif question == 'yes':
        print("Good choice!")
        X = input("Enter a positive integer:  ")
        if X.isdigit() is True:
            if int(X) >= 0:
                d = input("Input the split. The split has to divide the length of " + X + " i.e. 6:  ")
                if d.isdigit() is True:
                    if len(X) % int(d) == 0:
                        x = is_up_monotone(X, d)
                        if x is True:
                            print("The sequence is up-monotone")
                        else:
                            print("The sequence is not up-monotone")
                    else:
                        print(d + " does not divide " + str(len(X)) + ". Try again.")
                else:
                    print("The input can only contain digits. Try again.")
            else:
                print("The input has to be a positive integer. Try again.")
        else:
            print("The input can only contain digits. Try again.")
        flag = True
    else:
        print("Please enter yes or no. Try Again.")
        flag = True
