import binascii
def repXor(string, key):
    shex = binascii.hexlify(bytearray((string), "utf-8"))
    khex = binascii.hexlify(bytearray((key), "utf-8"))
    tmp = ""
    print(shex)
    print(khex)
    
    for i in range(len(string)):
        tmp += hex(ord(string[i]) ^ ord(key[i % len(key)]))[2:].zfill(2)
        #print(hex(ord(string[i]) ^ ord(key[i % len(key)]))[2:].zfill(2))
    return tmp

