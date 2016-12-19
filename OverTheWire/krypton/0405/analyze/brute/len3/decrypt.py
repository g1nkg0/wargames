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

    cipher1 = 'OYK'
    cipher2 = 'XIE'
    cipher3 = 'LGU'
    skeys1 = ''
    skeys2 = ''
    skeys3 = ''
    for i in range(0, len(cipher1)):
        skeys1 += chr(((ord(cipher1[i])-69)%26)+65)
    for i in range(0, len(cipher2)):
        skeys2 += chr(((ord(cipher2[i])-69)%26)+65)
    for i in range(0, len(cipher3)):
        skeys3 += chr(((ord(cipher3[i])-69)%26)+65)
    keys = itertools.product(skeys1, skeys2, skeys3)

    for k in keys:
        print(str(k) + '\n' + decrypt(infile, k) + '\n')

    #print(decrypt(infile, ''))
