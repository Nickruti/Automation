import itertools

with open("input.txt") as textfile1, open("input.txt") as textfile2: 
    for x, y in itertools.zip_longest(textfile1, textfile2):
        x = x.strip()
        y = y.strip()
        print("{0}\t{1}".format(x, y))