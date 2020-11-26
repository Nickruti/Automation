import itertools
import os
import time

with open('input.txt') as file1:
    for line1 in file1:
        with open('input.txt') as file2:
            for line2 in file2:
                   run = '"ffuf -w dir.txt -u ' + str(line2) + '-proxy ' + str(line1) + '"'
                   os.system(run)
                   time.sleep(5)