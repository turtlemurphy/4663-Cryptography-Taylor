###############################################
# Name: Taylor Murphy
# Class: CMPS 4663 Cryptography
# Date: 25 July 2015
# Program 2 - Randomized Vigenère Cipher
###############################################

import random
import re


#Possible Alphabets
#symbols = """ABCDEF"""
#symbols = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def buildVigenere(symbols):
    Tableau = open('tableau.txt', 'w')
       
    alphabetLen = len(symbols)
    vigenere = [[0 for i in range(alphabetLen)] for i in range(alphabetLen)]
    
    row = 0
    col = 0
    for i in range(alphabetLen * alphabetLen):

        vigenere[row][col] = chr(((col + row) % alphabetLen) + 32)
        col = col + 1
        
        if col >= alphabetLen:
            col = 0
            row = row + 1
            
    #Uncommenting the following line allows the Vigenere Tableau to be 
    #randomized however due to this randomization the first column of 
    #the Tableau contains repeats and as a result destoys the integrity 
    #of the encryption/decryption
            
    random.shuffle(vigenere)


    #write created vigenere matrix to a txt file 
    for l in vigenere:
        Tableau.write("%s\n" % l)

    return vigenere
    
def keywordFromSeed(seed):

    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 1000)))
        seed = seed // 1000
        
    return ''.join(Letters)
    
def keyByConcat(key):
    
    key = list(map(ord,key))
    encoded = 0
        
    for i in range(len(key)):
        encoded *= 1000        
        encoded += key[i]        

    return encoded     

def encrypt(plainTxtMessage, keyword):
    #build a randomized Vmatrix from symbols
    vigenere = buildVigenere(symbols)
    
    ctxt = []            
    
    keyword = list(keyword)
    plainTxtMessage = list(plainTxtMessage)
          
    for k in range(len(plainTxtMessage)):
        row = 0
        col = 0        
        keyRow = keyword[k % len(keyword)]
        messCol = plainTxtMessage[k]            
    
        for i in range(len(symbols)):
            if keyRow == vigenere[i][0]:
                row = i
                    
        for j in range(len(symbols)):
            if messCol == vigenere[0][j]:
                col = j      
                        
        ctxt.append(vigenere[row][col])
                
    ctxt = ''.join(ctxt)
    print("Cipher Text: ", ctxt)
    
    ciphertxt = open('encryptedText.txt', 'w')
    for letter in ctxt:
        ciphertxt.write("%s" % letter)
        
def decrypt(cipherTxtMessage, keyword):
    #build a randomized Vmatrix from symbols
    vigenere = buildVigenere(symbols)
    
    ptxt = []
    
    keyword = list(keyword)
    cipherTxtMessage = list(cipherTxtMessage)
    
    for k in range(len(cipherTxtMessage)):
        row = 0
        col = 0        
        keyRow = keyword[k % len(keyword)]
        messLetter = cipherTxtMessage[k]       
        
        for i in range(len(symbols)):
            if keyRow == vigenere[i][0]:
                row = i
                    
        for j in range(len(symbols)):
            if messLetter == vigenere[row][j]:
                col = j      
                        
        ptxt.append(vigenere[0][col])
                
    ptxt = ''.join(ptxt)
    print("Plain Text:  ", ptxt)
    
    plaintxt = open('decryptedText.txt', 'w')
    for letter in ptxt:
        plaintxt.write("%s" % letter)
