import csv
import io
import re

import re
hand = open('insulin.csv')

writeFile = open('preproinsulin-seq-clean.txt', 'w')
wrtFl1 = open('lsinsulin-seq-clean.txt', 'w')
wrtFl2 = open('binsulin-seq-clean.txt', 'w')
wrtFl3 = open('cinsulin-seq-clean.txt', 'w')
wrtFl4 = open('ainsulin-seq-clean.txt', 'w')

for line in hand:
    line = line.strip()
   # if re.search('ORIGIN', line):
    #   continue
    #else:
    x=re.sub(r'[^a-z]','',line)
    writeFile.write(x)

with open('preproinsulin-seq-clean.txt', 'r') as writeFile:
    str =  writeFile.readline()
    print(len(str.strip()))
    wrtFl1.write(str[0:24].strip())
    print(len(str[0:24].strip()))
    wrtFl2.write(str[24:54].strip())
    print(len(str[24:54].strip()))
    wrtFl3.write(str[54:90].strip())
    print(len(str[54:89]))
    wrtFl4.write(str[89:110])
    print(len(str[89:110]))    