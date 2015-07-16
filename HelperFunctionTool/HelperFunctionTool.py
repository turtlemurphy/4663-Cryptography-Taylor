###############################################
# Name: Taylor Murphy
# Helper Function Tool
###############################################
# Extended Euclidean algorithm 
#   returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
def egcd_r(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd_r(b % a, a)
        return (g, x - (b // a) * y, y)
        
# Extended Euclidean algorithm 
#   returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
def egcd_i(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# GCD
#   returns the greatest common denominator. Thats it.
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

# Mod Inverse V1
#   returns the modular multiplicative inverse (x) of a and m.
#   where ax = 1 (mod m) (= means congruent here)
def modinv(a, m):
    g, x, y = egcd_r(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
        
# Mod Inverse V2
#   returns the modular multiplicative inverse (x) of a and m.
#   where ax = 1 (mod m) (= means congruent here)
def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None # no mod inverse exists if a & m aren't relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

# Euler's totient function
#   returns some integer that represents the positive integers 
#   less than or equal to n that are relatively prime to n.
#def phi(n):
#    amount = 0
#
#    for k in range(1, n + 1):
#        if fractions.gcd(n, k) == 1:
#            #print(k)
#            amount += 1
#
#    return amount


###################################################################
#Start of Helper Function Tool

progStatus = '0'

print("Helper Function Tool")

while progStatus != '7':
    print("********************************************************")
    print("1. Extended Euclidean Algorithm-1")
    print("2. Extended Euclidean algorithm-2")
    print("3. Greatest Common Denominator")
    print("4. Mod Inverse-1")
    print("5. Mod Inverse-2")
    print("6. Euler's Totient Function")
    print("7. Quit")    
        
    progStatus = raw_input("Please select from the options above: ")
    print("********************************************************")    
    
    if progStatus == '1':
        # returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
        a = raw_input("a?: ")
        b = raw_input("b?: ")
        print (egcd_r(a, b))
            
    if progStatus == '2':    
        # returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
        a = raw_input("a?: ")
        b = raw_input("b?: ")
        print (egcd_i(a, b))
        
    if progStatus == '3':
        progStatus = '7'
    if progStatus == '4':
        progStatus = '7'
    if progStatus == '5':
        progStatus = '7'
    if progStatus == '6':
        progStatus = '7'
         
    
    if progStatus == '7':
        #exit program
        print("Exiting Helper Function, Goodbye")
