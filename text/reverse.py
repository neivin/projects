def reverse(s):
    l = len(s) - 1
    reverseStr = ""
    for i in xrange(l,-1,-1):
        reverseStr += s[i]
    return reverseStr

def main():
    s = raw_input("Enter a string to reverse: ")
    print "The reversed string is: " + reverse(s)

if __name__ == '__main__':
    main()
