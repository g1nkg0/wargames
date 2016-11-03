import sys
import string

def unigram(fileIn, fileOut):
    ret = open(fileOut, 'w')
    for char in string.uppercase:
        ret.write(char + ' ' + str(fileIn.count(char)) + '\n')

def occ(stringin, sub):
    count = start = 0
    while True:
        start = stringin.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def bigram(fileIn, fileOut):
    ret = open(fileOut, 'w')
    for char1 in string.uppercase:
        for char2 in string.uppercase:
            ret.write(char1 + char2 + ' ' + str(occ(fileIn, (char1 + char2))) + '\n')

if len(sys.argv) >= 3:
    file1 = open(sys.argv[1], 'r')
    file1 = file1.read()
    file2 = open(sys.argv[2], 'r')
    file2 = file2.read()

    unigram(file1, 'file1.1')
    unigram(file2, 'file2.1')

    bigram(file1, 'file1.2')
    bigram(file2, 'file2.2')
else:
    print 'Usage: ' + sys.argv[0] + ' /path/to/file1 file2 file3'
