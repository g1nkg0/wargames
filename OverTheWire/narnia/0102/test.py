#!/usr/bin/python
import string

out = ''
out += 'a'*128
for i in string.uppercase:
    out += i*4

print out
