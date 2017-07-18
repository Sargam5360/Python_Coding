#Input a line and count unique words in that line
import sys

for line in sys.stdin:
   # print line
    a = line.lower()
    b = a.split(',')
    myset = set(b)
    print len(myset)