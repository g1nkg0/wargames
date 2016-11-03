import itertools
import string
import enchant
import sys

if len(sys.argv) >= 2:
    alphabets = list(string.uppercase for i in range(6))
    d = enchant.Dict("en_US")

    file1 = open(sys.argv[1], 'r')
    file1 = file1.read(6)
    file2 = open(sys.argv[2], 'r')
    file2 = file2.read(6)

    for a in itertools.product(*alphabets):

        scheck1 = ''.join(list(chr(((ord(file1[n]) - ord(a[n])) % 26) + 65) for n in range(6)))
        scheck2 = ''.join(list(chr(((ord(file2[n]) - ord(a[n])) % 26) + 65) for n in range(6)))

        if d.check(scheck1):
            print("----------file1-------------\nKey: " + ''.join(a) + " Output: "+ scheck1 + "\n----------------------------\n")
        if d.check(scheck2):
            print("----------file2-------------\nKey: " + ''.join(a) + " Output: "+ scheck2 + "\n----------------------------\n")
else:
    print('Usage: ' + sys.argv[0] + ' file1 file2')
