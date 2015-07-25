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
         l1   = 12001907 % 100 = 7 = H
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
    
def keywordFromSeed(seed):

    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
        
    return ''.join(Letters)
    
def blockByConcat(message):
    
    message = list(map(ord,message))
    encoded = 999
        
    for i in range(len(message)):
        encoded *= 1000
        encoded += message[i]
        
    print (encoded)
    return encoded     

def encrypt(plain_text_message, keyword):
    pass
        
def decrypt(cipher_text_message, keyword):
    pass


message = 'MATH'

blockByConcat(message)

keyWord = keywordFromSeed(999077065084072)
print(keyWord)

#char = chr((25) % 26 + 65)
#print (char)



            
