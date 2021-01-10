def min_enclosing_rectangle(radius, x, y):
    """
    (number, number, number) -> (number, number)
    Takes 3 numbers, radius, x, and y, and returnes the coordinates of the x and y coordinates of the bottom left point of the rectangle.
    Preconditions: radius, x, and y are numbers.
    """
    if radius < 0:
        return None
    else:
        return (x - radius, y - radius)


def vote_percentage(results):
    """
    (str)-> float
    Takes a string of votes, results, and counts number of 'yes' and 'no' and returns the percentage of yes votes.
    Preconditions: results consist of only yes, no or abstained
    """
    yes = results.count('yes')
    no = results.count('no')
    return yes/(no + yes)


def vote():
    """
    ()-> str
    Takes an input of votes from user, calls the vote_percentage(results) function and returns a string based on the proportion of yes votes.
    """
    v = input("Enter the yes, no, and abstained votes one by one and then press enter:\n")
    p = vote_percentage(v)
    if p == 1:
        print("Proposal passes unanimously.")
    elif p > 2/3 or p == 2/3:
        print("Proposal passes with super majority.")
    elif p > 1/2 or p == 1/2:
        print("Proposal passes with simple majority.")
    else:
        print("Proposal fails.")

