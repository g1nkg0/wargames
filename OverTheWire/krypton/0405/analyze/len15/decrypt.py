import sys
import string
import itertools

def decrypt(ciphertxt, key):
    ret = ''
    for i, c in enumerate(ciphertxt):
        ret += chr((ord(c) - ord(key[i % len(key)])) % 26 + 65)
    return ret

if (len(sys.argv) < 2):
    print("Usage: " + sys.argv[0] + " filetodecrypt")
else:
    infile = open(sys.argv[1], 'r')
    infile = infile.read()
    infile = infile.rstrip('\n')

    keys = itertools.product('OYK', 'XIE', 'LGU')

    for k in keys:
        #print(str(k) + '\n' + decrypt(infile, k) + '\n')

    #print(decrypt(infile, ''))
