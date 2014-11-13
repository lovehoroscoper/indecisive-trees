import sys

for line in sys.stdin:
    dictionary ={}
    line = line.strip()
    tokens = line.split('\t')
    tokenlist = tokens[1].split("|")
    dictionary[tokens[0]] = tokenlist
    print dictionary
