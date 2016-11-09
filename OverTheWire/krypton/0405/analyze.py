import sys
import string

def countnth(listofstrings, n, c):
    fileout = 'count.' + str(n) + '.' + str(c)
    allnth = ''
    for i in range(0, len(listofstrings)):
        allnth += listofstrings[i][n]

    unigram(allnth, fileout)

def unigram(fileIn, fileOut):
    ret = open(fileOut, 'w')
    for char in string.uppercase:
        ret.write(str(fileIn.count(char)).zfill(2) + ' ' + char + '\n')

if len(sys.argv) >= 4:
    for c in range(1, 16):
        file1 = open(sys.argv[1], 'r')
        file1 = file1.read()
        file1.rstrip('\n')
        file1 = [file1[i:i+c] for i in range(0, len(file1), c)]
        file1 = file1[:len(file1)-1]

        file2 = open(sys.argv[2], 'r')
        file2 = file2.read()
        file2.rstrip('\n')
        file2 = [file2[i:i+c] for i in range(0, len(file2), c)]
        file2 = file2[:len(file2)-1]

        file3 = open(sys.argv[3], 'r')
        file3 = file3.read()
        file3.rstrip('\n')
        file3 = [file3[i:i+c] for i in range(0, len(file3), c)]
        file3 = file3[:len(file3)-1]

        for i in range(0, c):
            countnth(file1, i, c)

        for i in range(0, c):
            countnth(file2, i, c)

        for i in range(0, c):
            countnth(file2, i, c)

else:
    print 'Usage: ' + sys.argv[0] + ' /path/to/file1 file2 file3'
