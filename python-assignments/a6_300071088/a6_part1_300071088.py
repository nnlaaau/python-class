import string


def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    flag = True
    while flag:
        try:
            filename = input('Please enter the name of your file: ')
            fileopen = open(filename)
            flag = False
            return fileopen
        except FileNotFoundError:
            print('There is no file with that name. Please try again.')


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    dicto = {}
    sent = fp.read()
    spag = str.maketrans(dict.fromkeys(string.punctuation))
    sent = sent.translate(spag)
    sentlst = sent.split('\n')
    counter = 1
    for i in sentlst:
        if len(i) > 0:
            words = i.strip().lower().split(' ')
            for x in words:
                w = x
                if w in dicto:
                    dicto[w].add(counter)
                else:
                    dicto[w] = {counter}
        counter += 1
    return dicto


def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    qry = query.split(' ')
    co = []
    for i in qry:
        if i in D:
            co.append(D[i])
    if len(co) == 0:
        return None
    return list(set.intersection(*co))


##############################
# main
##############################
file = open_file()
d = read_file(file)

# YOUR CODE GOES HERE
flag = True
while flag:
    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    if query != 'q':
        out = find_coexistance(d, query)
        res = ''
        if out is None:
            print('Word ' + query + ' is not in the file.')
        elif len(out) > 0:
            for i in range(len(out)):
                res = res + str(out[i]) + ' '
            print('The one or more words you entered coexisted in the following lines of the file: ')
            print(res)
    elif query == 'q':
        flag = False
