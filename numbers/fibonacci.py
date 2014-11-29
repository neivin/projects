def fibonacci(n):
    a = 0
    b = 1
    print a,
    print b,
    for i in xrange(n-2):
        c = a + b
        print c,
        a = b
        b = c

def main():
    n = raw_input("Enter how many Fibonacci numbers you want: ")
    fibonacci(int(n))
    
if __name__ == '__main__':
    main()
