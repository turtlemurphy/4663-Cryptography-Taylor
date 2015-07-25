###############################################
# Name: Taylor Murphy
# Class: CMPS 4663 Cryptography
# Date: 25 July 2015
# Program 2 - Randomized Vigenère Cipher
###############################################

import random

"""
keywordFromSeed -
    Works by peeling off two digits at a time, and using modulo to map it into
    the proper range of A-Z for use as a keyword.

# Example:
    This example spells math, and I chose values 0-25 on purpose, but
    it really doesn't matter what values we choose because 99 % 26 = 21 or 'V' 
    or any value % 26 for that matter.

    S1:  seed = 12001907
         l1   = 12001907 % 100 = 07 = H
         seed = 12001907 // 100 = 120019
    
    S2:  l2   = 120019 % 100 = 19 = T
         seed = 120019 // 100 = 1200
    
    S3:  l3   = 1200 % 100 = 0 = A
         seed = 1200 // 100 = 12
    
    S4:  l4   = 12 % 100 = 12 = M
         seed = 12 // 100 = 0

    @param {int} seed - An integer value used to seed the random number 
                        generator that we will use as our keyword for vigenere
    @return {string} keyword - a string representation of the integer seed
#############################################################################
"""
def keywordFromSeed(seed):

    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
        
    return ''.join(Letters)

#Describes itself
def encrypt(plain_text_message,keyword):
    pass
        
#Describes itself
def decrypt(cipher_text_message,keyword):
    pass

"""           
This will build and return the Vigenere matrix.
You don't need to pass the seed or anything 
for that matter to the function because once 
the random number generator has been seeded 
once at the top of the program, you don't have
to worry about seeding anymore.

Twist! Your vigenere cipher tableau will be a 
95 x 95 matrix using the following symbols:
"""
def buildVigenere(symbols):
    n = len(symbols)

    vigenere = [[0 for i in range(n)] for i in range(n)]

    #Build the vigenere matrix
    for i in range(n):
        temp = symbols
        
        for j in range(n):
            r = random.randrange(len(temp))
            vigenere[i][j] = temp[r]
            temp.replace(temp[r],'')
            
    return vigenere




            
