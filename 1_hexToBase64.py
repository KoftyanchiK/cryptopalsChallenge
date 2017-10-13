# Hexadecimal string to binary
def hexToBin(hex):
	map = {
		'0': "0000",
		'1': "0001",
		'2': "0010",
		'3': "0011",
		'4': "0100",
		'5': "0101",
		'6': "0110",
		'7': "0111",
		'8': "1000",
		'9': "1001",
		'a': "1010",
		'b': "1011",
		'c': "1100",
		'd': "1101",
		'e': "1110",
		'f': "1111"
	}
	if ((hex[1] == 'x' or hex[1] == 'X') and hex[0] == '0'):
		hex = hex[2:]
	result = ""
	for char in hex:
		if (char.lower() in map.keys()):
			result += map[char.lower()]
		else:
			raise ValueError("No such key %s in maping", char)
	return result
	
# From binary string to decimal
def binToDec(binary):
	result = 0;
	length = len(binary)
	for i in range(length, 0, -1):
		if (binary[i - 1] == '0' or binary[i - 1] == '1'):
			result += int(binary[i - 1]) * (2 ** (length - i))
		else:
			raise ValueError("Binary string should contain only 0 or 1 symbols")
	return result

# Binary string to base64 code
def binToBase64(binary):
    alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    result = ""
    if (len(binary) % 6 != 0):
    	binary += '0' * (6 - len(binary) % 6)
    first = 0
    last = 6
    for seq in range(0, len(binary), 6):
    	result += alphas[binToDec(binary[first:last])]
    	first = last
    	last = last + 6
    return result

def hexToBase64(hexadecimal):
	return binToBase64(hexToBin(hexadecimal))

#binToDec("101")
#print(hexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))


