def longest_run(l):
    """
    (list of int)-> int
    Takes a list of numbers, l, and returns the length of the longest run.
    Preconditions: the list should contain multiple, real integers.
    """
    maxed = 0
    ct = 1
    for i in range(1, len(l)):
        if l[i] != l[i-1]:
            if ct > maxed:
                maxed = ct
            ct = 1
        else:
            ct += 1
    if len(l) > 0 and ct > maxed:
        maxed = ct
    return maxed


# Main
l = input("Please input a list of integers separated by spaces: ").strip().split()

