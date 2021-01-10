def number_divisible(l, n):
    """
    (list of int, int) -> int
    Takes a list of integers, l and a non-zero integer, n as input, and returns the number of elements in the list that are divisible by n.
    Preconditions: L is a list of real numbers, and n is a non-zero integer.
    """
    flag = 0
    for i in range(0, len(l)):
        if int(l[i]) % n == 0:
            flag += 1
    return flag


# Main
l = input("Please enter a list of numbers separated by a space: ").strip().split()
n = int(input("Please enter a non-zero integer: "))
print(number_divisible(l, n))
