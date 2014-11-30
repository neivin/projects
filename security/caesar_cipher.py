## Implement a Caesar cipher, both encoding and decoding. 
## The key is an integer from 1 to 25. This cipher rotates the letters
## of the alphabet (A to Z). The encoding replaces each letter with the 
## 1st to 25th next letter in the alphabet (wrapping Z to A). 
## So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC". 
## This simple "monoalphabetic substitution cipher" provides almost 
## no security, because an attacker who has the encoded message can 
## either use frequency analysis to guess the key, or just try all 25 keys.

def codify(str, key, cmd):
    encList = [None] * 26
    encodedStr = ""
    
    for i in range(26):
        if cmd == "en":
            encList[i] = (i + key) % 26
        else:
            encList[i] = (i - key) % 26
    
    for i in range(len(str)):
        num = ord(str[i])
        if num > 96 and num < 123:
            num -= 97
            encodedNum = encList[num] + 97
            encodedStr += chr(encodedNum)
        else:
            encodedStr += str[i]
        
    return encodedStr

def main():
    cmd = "de"
    while True:
        choice = raw_input("Do you want to encode, or decode a string? (e/d): ")
    
        if choice == 'e':
            cmd = "en"
        
        key = 0
        while True:
            key = raw_input("Enter a key for the Caesar Cipher(1-25): ")
            if int(key) >0 and int(key) <26:
                break
            else:
                print "Sorry! Please enter a valid key from 1 - 25"
    
        str = raw_input("Enter the phrase you want coded: ")
        newStr = codify(str, int(key), cmd)
        
        print "The " + cmd + "coded phrase is: " + newStr + "\n"
        
        choice2 = raw_input("Would you like to code something else: (y/n) ")
        
        if choice2 == "n":
            print "Goodbye!"
            break
    
if __name__ == '__main__':
    main()

