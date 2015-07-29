###############################################
# Name: Taylor Murphy
# Class: CMPS 4663 Cryptography
# Date: 25 July 2015
# Program 2 - Randomized Vigenère Cipher
###############################################

import random

#Possible Alphabets
#symbols = """ABCDEF"""
#symbols = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def buildVigenere(symbols):
    Tableau = open('tableau.txt', 'w')
       
    #Creates and empty Vmatrix based on size of symbols to be filled later
    alphabetLen = len(symbols)
    vigenere = [[0 for i in range(alphabetLen)] for i in range(alphabetLen)]
    
    #loads vigenere with the range of characters defined above
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
    #the Tableau can contain repeats (based on the strength of the seed) 
    #and as a result it can destroy the integrity of the encryption/decryption
    random.shuffle(vigenere)

    #write created vigenere matrix to a txt file 
    for l in vigenere:
        Tableau.write("%s\n" % l)

    return vigenere
    
def keywordFromSeed(seed):
    #This function translates the given seed into a character ranging from
    #32 to 126 on the ASCII table
    #Note: this function takes 3 numbers from the back of the seed and finds its
    #character equivalent
    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 1000)))
        seed = seed // 1000
        
    return ''.join(Letters) 

def encrypt(plainTxtMessage, keyword):
    #This function takes the plaintxt message and the keyword and uses the
    #Vigenère algorithm to encrypt the message 
    
    #build a randomized Vmatrix from symbols
    vigenere = buildVigenere(symbols)
    
    ctxt = []            
    
    #changes the keyword and message to a list for ease of use
    keyword = list(keyword)
    plainTxtMessage = list(plainTxtMessage)
          
    #Uses the keyword to find the encrypting row and the message
    #to find the encrypting column, then assigns vigenere[row][col] 
    #to the ctxt list   
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
                
    #changes the ctxt list into a string for printability 
    ctxt = ''.join(ctxt)
    print("Cipher Text: ", ctxt)
    
    #writes the ctxt string to a file for future use by the decrypt function
    ciphertxt = open('encryptedText.txt', 'w')
    for letter in ctxt:
        ciphertxt.write("%s" % letter)
        
def decrypt(cipherTxtMessage, keyword):
    #This function takes the ciphertxt message and the keyword and uses the
    #Vigenère algorithm to decrypt the message    
    
    #build a randomized Vmatrix from symbols
    vigenere = buildVigenere(symbols)
    
    ptxt = []
    
    #changes the keyword and ctxt to a list for ease of use
    keyword = list(keyword)
    cipherTxtMessage = list(cipherTxtMessage)
    
    #Uses the keyword to find the decrypting row and the message
    #to find the decrypting column within that same row, then 
    #assigns vigenere[0][col] to the ptxt list    
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
                
    #changes the ptxt list into a string for printability
    ptxt = ''.join(ptxt)
    print("Plain Text:  ", ptxt)
    
    #writes the ptxt string to a file for future use
    plaintxt = open('decryptedText.txt', 'w')
    for letter in ptxt:
        plaintxt.write("%s" % letter)
