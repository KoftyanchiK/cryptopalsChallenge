import base64

KEYSIZE_MAX = 40

def strToBin(string):
	return "".join('{:08b}'.format(ord(x), 'b') for x in string)

def getHammingDistance(str1, str2):
	if (len(str1) != len(str2)):
		raise ValueError("Strings must be of equal size")
	str1 = strToBin(str1)
	str2 = strToBin(str2)
	dist = 0
	# print(str1, str2)
	# print(len(str1))
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			dist += 1

	return dist

# Test Hamming distance
# print(getHammingDistance("this is a test", "wokka wokka!!!"))

# Make base64 conversion to ascii string
file = open("6task", "r")
base64_string = ""
for line in file:
	base64_string += line
string = base64.b64decode(base64_string)

# print(string)
for i in range(2, KEYSIZE_MAX):
	# Do some magic