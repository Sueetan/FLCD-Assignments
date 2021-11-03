import re


def read_tokens(file):
    operators = []
    separators = []
    reserverd_words = []

    filee = open(file, 'r')

    for i in range(11):
        operators.append(filee.readline().strip())
    for i in range(8):
        separators.append(filee.readline().strip())
    for i in range(12):
        reserverd_words.append(filee.readline().strip())

    return operators, separators, reserverd_words

def check_ident(element):
    check = re.compile('^[a-zA-Z]([a-zA-Z0-9])*$')
    return check.match(element) is not None

def check_const(element):

    intt = re.compile('^[1-9]([0-9])*$')

    charr = re.compile("^\'[a-zA-Z0-9\.,]\'$")

    stringg = re.compile("^\"[a-zA-Z0-9\.,]*\"$")

    if intt.match(element) is not None:
        return True
    if charr.match(element):
        return True
    if stringg.match(element):
        return True
    return False

