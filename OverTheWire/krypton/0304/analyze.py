import sys
import string

def countnth(listofstrings, n):
    fileout = 'count.' + str(n)
    allnth = ''
    for i in range(0, len(listofstrings)):
        allnth += listofstrings[i][n]

    unigram(allnth, fileout)

def unigram(fileIn, fileOut):
    ret = open(fileOut, 'w')
    for char in string.uppercase:
        ret.write(str(fileIn.count(char)).zfill(2) + ' ' + char + '\n')

if len(sys.argv) >= 3:
    file1 = open(sys.argv[1], 'r')
    file1 = file1.read()
    file1.rstrip('\n')
    file1 = [file1[i:i+6] for i in range(0, len(file1), 6)]
    file1 = file1[:len(file1)-1]
    print(file1)

    file2 = open(sys.argv[2], 'r')
    file2 = file2.read()
    file2.rstrip('\n')
    file2 = [file2[i:i+6] for i in range(0, len(file2), 6)]
    file2 = file2[:len(file2)-1]
    print(file2)

    for i in range(0, 6):
        countnth(file1, i)

    for i in range(0, 6):
        countnth(file2, i)

else:
    print 'Usage: ' + sys.argv[0] + ' /path/to/file1 file2 file3'
