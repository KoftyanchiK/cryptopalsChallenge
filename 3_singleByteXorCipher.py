import binascii
def singleByteXor(encrypted):
    enc = encrypted.strip()

    nums = binascii.unhexlify(enc)
    # Define a probability of each char from english aplphabet
    prob = {'a': 0.08166999999999999, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06326999999999999, 't': 0.09055999999999999, 'u': 0.02758, 'v': 0.00978, 'w': 0.0236, 'x': 0.0015, 'y': 0.01974, 'z': 0.00074}
    # Define key=>value storage for valid strings (where only ascii chars) and rating
    tmpranges = {}

    # For each symbol
    for c in range(256):
        tmp = ""
        # Fill tmp string with c XORed with each symbol from enc string
        for i in nums:
            tmp += chr(i ^ c)
        # Define dictionary for probability of each sym in decoded string
        count = dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"), 0.0000)
        tmp = tmp.lower()
        tmpranges[tmp] = 0 # Set rating to 0
        # Count all chars
        for i in tmp:
            if i in list("abcdefghijklmnopqrstuvwxyzv"):
                count[i] += 1
            elif i in list(",.':;!? "):
                continue
            else:
                break
                
        # Transform in probability format
        for i in count:
            count[i] = count[i]/24
            # And if probabilities are equal increase rating on 1
            if count[i] >= prob[i]:
                tmpranges[tmp] += 1

    # Find string with max rating
    max_val = max(tmpranges.values())
    for s in tmpranges:
        if tmpranges[s] == max_val and tmpranges[s] >= 10:
            print(s)
            return True
        #print(count)

#singleByteXor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
