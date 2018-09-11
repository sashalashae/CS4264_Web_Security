from roots import *
import hashlib
import sys
message = sys.argv[1]
# Your code to forge a signature goes here.

#######################################################

prefix = '0001FF003021300906052B0E03021A05000414'

shaMsg = hashlib.sha1()
shaMsg.update(message)
sha1Msg = shaMsg.hexdigest()

msgStr = prefix + sha1Msg

totalHexChars = 256*2

lengthOfPaddingChar = totalHexChars - len(msgStr)
padding = ''

for i in range(0, lengthOfPaddingChar):
	padding = padding + '0'

totalStr = msgStr + padding

intStr = int(totalStr, 16)

intValue, boolValue = integer_nthroot(intStr, 3)

if boolValue == 0:
	intvalue = intValue + 1

#######################################################

print integer_to_base64(intValue)