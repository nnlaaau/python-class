def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name = input("Enter the name of the file: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name = None
    return file_name


def get_file_name():
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


def clean_word(word):
    """
    (str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed
    """
    clean = ''
    excluding = '!.?:,"-_\()[]{}%123456789'+"'"
    for wrd in word:
        if wrd not in excluding:
            clean += wrd
    return clean.lower().strip()


def test_letters(w1, w2):
    """
    (str,str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise
    """
    w1 = list(w1)
    w2 = list(w2)

    if sorted(w1) == sorted(w2):
        return True
    else:
        return False


def create_clean_sorted_nodupicates_list(s):
    """
    (str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)
    """
    new = []
    s = clean_word(s).split()
    for word in s:
        if word not in new:
            new.append(word)
    new.sort()
    return new


def word_anagrams(word, wordbook):
    """
    (str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function should call test_letters function.

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook
    """
    anagrams = []
    for i in wordbook:
        if test_letters(i, word):
            anagrams.append(i)
    if word in anagrams:
        anagrams.remove(word)
    return sorted(anagrams)


def count_anagrams(l, wordbook):
    """(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.
    
    Whenever a word in l is the same as a word in wordbook, that is not counted.
    """
    counted = []
    for i in l:
        x = len(word_anagrams(i, wordbook))
        counted.append(x)
    return counted


def k_anagram(l, anagcount, k):
    """(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)
    """
    kanagram = []
    for i in range(0, len(anagcount)):
        if k == anagcount[i]:
            kanagram.append(l[i])
    return kanagram


def max_anagram(l, anagcount):
    """
    (list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)
    """
    i = 0
    big = anagcount[0]
    while i <= len(anagcount) - 1:
        if big >= anagcount[i]:
            i += 1
        else:
            big = anagcount[i]
            i += 1
    maxed = k_anagram(l, anagcount, big)
    return maxed


def zero_anagram(l, anagcount):
    """
    (list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)
    """
    zerod = k_anagram(l, anagcount, 0)
    return zerod


##############################
# main
##############################
wordbook = open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("Would you like to:")
print("1. Analize anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice = input()

if choice == '1':
    file_name = get_file_name()
    rawtx = open(file_name).read()
    l = create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l, wordbook)

    maxed = max_anagram(l, anagcount)

    print("\nOf all the words in your file, the following words have the most anagrams:")
    print(maxed)

    print("\nHere are their anagrams:")
    for z in range(0, len(maxed)):
        print("Anagrams of", maxed[z], "are: ", word_anagrams(maxed[z], wordbook))

    print("\nHere are the words from your file that have no anagrams:")
    print(zero_anagram(l, anagcount))

    print("\nSay you are interested if there is a word in your file that has exactly k anagrams.")
    k = int(input("Enter a positive integer: "))
    print("Here is a word (words) in your file with exactly", k, "anagrams:")
    print(k_anagram(l, anagcount, k))

elif choice == '2':
    c = input("Enter the letters that you have, one after another with no space:\n").lower()
    flag = True
    while flag:
        if " " not in c:
            flag = False
        else:
            print("Error: You entered space(s).")
            c = input("Enter the letters that you have, one after another with no space:\n").lower()
    y = int(input("Would you like help forming a word with\n1. all these letters\n2. all but one of these letters?\n"))
    if y == 1:
        d = word_anagrams(c, wordbook)
        if len(d) == 0:
            print("There is no word comprised of exactly these letters.")
        else:
            if c in wordbook:
                d.append(c)
                d.sort()
                print("Here are all the words that are comprised of exactly these letters:\n", d)
            else:
                print("Here are all the words that are comprised of exactly these letters:\n", d)
    elif y == 2:
        print("The letters you gave us are: ", c)
        count = 0
        while count <= len(c) - 1:
            new = ''
            for s in range(0, len(c)):
                if s != count:
                    new += c[s]
            print("Without the letter in position", count + 1, "we have letters:", new)
            j = word_anagrams(new, wordbook)
            if new in wordbook:
                j.append(new)
                j.sort()
            if len(j) == 0:
                print("There is no word comprised of letters:", new)
            else:
                print("Here are the words that are comprised of the letters:", new, "\n", j)
            count += 1

else:
    print("Good bye")
