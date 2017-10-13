from hexToBase64 import *

# Xor two hexadecimal buffers
def fixedXor(buf_1, buf_2):
	if (len(buf_1) != len(buf_2)):
		raise ValueError("Buffers must be of equal length")
	buf_1 = hexToBin(buf_1)
	buf_2 = hexToBin(buf_2)
	length = len(buf_1)
	result = ""
	for i in range(length):
		result += str(int(buf_1[i]) ^ int(buf_2[i]))
	return hex(int(result, 2))[2:]