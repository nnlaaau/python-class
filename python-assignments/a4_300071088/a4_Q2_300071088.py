def two_length_run(l):
    """
    (list of int) -> bool
    Takes a list of numbers as an input and returns True if given list has at least one run, and false otherwise.
    Preconditions: l must be a list of real numbers.
    """
    for i in range(0, len(l)-1):
        if l[i] == l[i + 1]:
            return True
    return False


# Main
l = input("Enter a list of numbers separated by space: ").strip().split()
print(two_length_run(l))