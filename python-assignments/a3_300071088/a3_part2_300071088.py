def sum_odd_divisors(n):
    """
    (int) -> (int)
    Takes an int n as input and returns the sum of all positive odd divisors of n.
    Preconditions: n is an integer
    """
    s = 0
    if n == 0:
        return None
    else:
        if n < 0:
            n = abs(n)
        for i in range(1, n + 1):
            if n % i == 0 and n % 2 != 0:
                s = s + i
    return s


def series_sum():
    """
    (none) -> number
    Asks user for a non-negative integer, n and returns the sum of the series.
    Preconditions: n is a non-negative integer.
    """
    x = int(input("Enter a non-negative integer: "))
    if x < 0:
        return None
    else:
        a = 1000
        for i in range(1, x + 1):
            a = a + (1 / i ** 2)
    return a


def pell(n):
    """
    Takes an int n, and returns the nth Pell number.
    Precondition: n is a non-negative integer.
    """
    if n < 0:
        return None
    pass

def countMembers(s):
    """
    (str)-> int
    Takes a string and returns the number of characters that appear in the string.
    Preconditions: No string methods.
    """
    counter = 0
    for x in s:
        if 'e' <= x <= 'j' or 'F' <= x <= 'X' or '2' <= x <= '6' or x == '!' or x == ',' or x == '\\':
            counter = counter + 1
    return counter


def casual_number(s):
    """
    (str) -> number
    Takes a string, s, and returns an integer representing the number in s.
    """
    a = ""
    x = 0
    for char in range(len(s)):
        if s[char] == ',':
            a = a
        elif s[char].isdigit():
            a = a + s[char]
            x = 1
        elif s[char] == '-':
            a = a + s[char]
        else:
            return None
    if x == 1:
        return int(a)
    else:
        return None


def alienNumbers(s):
    """
    (str)-> int
    Takes a str, s, and returns a number based on the alien numbering system tables.
    """
    a = 0
    for i in s:
        if i == "T":
            a = a + 1024
        elif i == "y":
            a = a + 598
        elif i == "!":
            a = a + 121
        elif i == "a":
            a = a + 42
        elif i == "N":
            a = a + 6
        elif i == 'U':
            a = a + 1
        else:
            a = a + 0
    return a


def alienNumbersAgain(s):
    """
    (str) -> int
    Takes  a string, s and returns the numeric value using the alien numbering system.
    """
    n = 0
    counter = 0
    for i in s:
        counter = counter + 1
    i = 0
    while i < counter:
        n = n + alienNumbers(s[i])
        i = i + 1
    return n


def encrypt(s):
    """
    (str) -> str
    Takes a string s and returns a scrambled string.
    """
    x = ""
    a = int(len(s))
    for i in range(int(a/2)):
        x = x + s[len(s) - 1 - i] + s[i]
    if a % 2 != 0:
        x = x + s[a / 2]
    return x


def weaveop(s):
    """
    (str)->str
    Takes an string, s and returns a string with o and p inserted between every consecutive characters of s.
    """
    x = ""
    for i in range(0, len(s) - 1):
        x = x + s[i]
        if s[i].isalpha() and s[i + 1].isalpha():
            if s[i].isupper():
                x = x + 'O'
            else:
                x = x + 'o'
        if s[i].isalpha() and s[i + 1].isalpha():
            if s[i + 1].isupper():
                x = x + 'P'
            else:
                x = x + 'p'
    x = x + s[-1]
    return x


def squarefree(s):
    """
    (str)-> bool
    Takes a string, s and returns whether it is a squarefree number or not.
    """
    pass