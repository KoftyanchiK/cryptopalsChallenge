from singleByteXorCipher import *

file = open("4task", "r")
for line in file:
    if (singleByteXor(line)):
        print(line)
        print("done\n")
