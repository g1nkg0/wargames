import sys
import string
import itertools
import enchant

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

    cipher1 = 'YOZ'
    cipher2 = 'XIS'
    cipher3 = 'BUC'
    cipher4 = 'OYK'
    cipher5 = 'XME'
    cipher6 = 'GRL'
    skeys1 = ''
    skeys2 = ''
    skeys3 = ''
    skeys4 = ''
    skeys5 = ''
    skeys6 = ''
    for i in range(0, len(cipher1)):
        skeys1 += chr(((ord(cipher1[i])-69)%26)+65)
    for i in range(0, len(cipher2)):
        skeys2 += chr(((ord(cipher2[i])-69)%26)+65)
    for i in range(0, len(cipher3)):
        skeys3 += chr(((ord(cipher3[i])-69)%26)+65)
    for i in range(0, len(cipher4)):
        skeys4 += chr(((ord(cipher4[i])-69)%26)+65)
    for i in range(0, len(cipher5)):
        skeys5 += chr(((ord(cipher5[i])-69)%26)+65)
    for i in range(0, len(cipher6)):
        skeys6 += chr(((ord(cipher6[i])-69)%26)+65)
    keys = itertools.product(skeys1, skeys2, skeys3, skeys4, skeys5, skeys6)

    d = enchant.Dict("en_US")
    for k in keys:
        dec = decrypt(infile, k)
        for i in range(6):
            chk = dec[:i]
            if d.check(chk):
                print(str(k) + '\n' + decrypt(infile, k) + '\n')
                continue

    #print(decrypt(infile, ''))
