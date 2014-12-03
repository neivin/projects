def toBinary (dec):
    binNum = ""
    while (dec > 0):
        digit = dec % 2
        binNum = str(digit) + binNum
        dec /= 2
    return binNum

def toDec (bin):
    decNum = 0
    for i in xrange(len(str(bin))):
        digit = bin % 10
        decNum += digit * (2 ** i)
        bin /= 10
        
    return decNum