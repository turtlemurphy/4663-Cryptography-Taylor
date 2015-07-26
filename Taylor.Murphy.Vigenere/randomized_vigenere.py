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
    Tableau = open('tableau.txt', 'w')
    
    alphabetLen = len(symbols)
    vigenere = [[0 for i in range(alphabetLen)] for i in range(alphabetLen)]

    #Build the vigenere matrix
    for i in range(alphabetLen):
        temp = symbols
        for j in range(alphabetLen):
            r = random.randrange(len(temp))
            vigenere[i][j] = temp[r]
            temp.replace(temp[r],'')
    
    #write created vigenere matrix to a txt file 
    for letter in vigenere:
        Tableau.write("%s\n" % letter)
            
    return vigenere
    
def keywordFromSeed(seed):

    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 100)))
        seed = seed // 100
        
    return ''.join(Letters)
    
def keyByConcat(message):
    
    message = list(map(ord,message))
    encoded = 0
        
    for i in range(len(message)):
        encoded *= 100        
        encoded += message[i]        

    return encoded     

def encrypt(plain_text_message, keyword):
    pass
        
def decrypt(cipher_text_message, keyword):
    pass

#test block
###############################################

#symbols = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
#symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
#
#print (len(symbols))
#print (symbols.index('A'))
#message = """ !"#$%&'()*+,-./"""
#
#keyWord = keywordFromSeed(keyByConcat(message))
#print(keyWord)
#
#char = chr((25) % 26 + 65)
#print (char)



            
