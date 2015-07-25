###############################################
# Name: Taylor Murphy
# Class: CMPS 4663 Cryptography
# Date: 13 July 2015
# Program 1 - Playfair Cipher
###############################################

import re

#Start of function definitions

def generateAlphabet():
    #Create empty alphabet string
    alphabet = ""
    
    #Generate the alphabet
    for i in range(0,26):
        alphabet = alphabet + chr(i+65)
        
    return alphabet


def cleanString(s,options = {'up':1,'reNonAlpha':1,'reSpaces':'','spLetters':'X'}):
    """
    Cleans message by doing the following:
    - up            - uppercase letters
    - spLetters     - split double letters with some char
    - reSpaces      - replace spaces with some char or '' for removing spaces
    - reNonAlpha    - remove non alphabetic characters
    - reDupes       - remove duplicate letters

    @param   string -- the message
    @returns string -- cleaned message
    """
    if 'up' in options:
        s = s.upper()
        
    if 'spLetters' in options:
        #replace 2 occurences of same letter with letter and 'X'
        s = re.sub(r'([A-Z])\1', r'\1X\1', s)
        
    if 'reSpaces' in options:
        space = options['reSpaces']
        s = re.sub(r'[\s]', space, s)
    
    if 'reNonAlpha' in options:
        s = re.sub(r'[^A-Z]', '', s)
        
    if 'reDupes' in options:
        s= ''.join(sorted(set(s), key=s.index))
        
    return s

def generateSquare(key):
    """
    Generates a play fair square with a given keyword.

    @param   string   -- the keyword
    @returns nxn list -- 5x5 matrix
    """
    row = 0     #row index for sqaure
    col = 0     #col index for square
    
    #Create empty 5x5 matrix 
    playFair = [[0 for i in range(5)] for i in range(5)]
    
    alphabet = generateAlphabet()
    
    #uppercase key (it meay be read from stdin, so we need to be sure)
    key = cleanString(key,{'up':1,'reSpaces':'','reNonAlpha':1,'reDupes':1})
    
    #Load keyword into square
    for i in range(len(key)):
        playFair[row][col] = key[i]
        alphabet = alphabet.replace(key[i], "")
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    #Remove "J" from alphabet
    alphabet = alphabet.replace("J", "")
    
    #Load up remainder of playFair matrix with 
    #remaining letters
    for i in range(len(alphabet)):
        playFair[row][col] = alphabet[i]
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    return playFair

def getCoords(playfair, char):
    row = 0
    col = 0
    #loop through playfair until char is found 
    #then return the coords (row, col)
    for i in range(5):
        for j in range(5):
            if playfair[i][j] == char:
                row = i
                col = j
    return row, col

def ptxtDigrapher(ptxt):
    digraphArr = []
    
    # Load chars from ptxt into digraphArr
    for char in ptxt:
        digraphArr.append(char)
    
    #if the # of chars in digraphArr is odd add an X to the last digraph
    if len(digraphArr)%2 == 1:
        digraphArr.append("X")

    #Load digraphs into ptxtDigraphs
    i = 0
    ptxtDigraphs = []
    for x in range(1, (len(digraphArr)/2) + 1):
        ptxtDigraphs.append(digraphArr[i:i + 2])
        i = i + 2
        
    return ptxtDigraphs

def ctxtDigrapher(ctxt):
	i = 0
	ctxtDigraphs=[]
     #works the same way as ptxtDigrapher but with fewer conditions
	for count in range(len(ctxt)/2):
		ctxtDigraphs.append(ctxt[i:i+2])
		i = i + 2
  
	return ctxtDigraphs
    
def encrypt(ptxt, playfair):
    #convert ptxt string into ptxt array holding the digraph pairs
    ptxt = ptxtDigrapher(ptxt)
    ciphertext=[]
    
    #for each digraph in ptxt
    for di in ptxt:
        #extract the row and col coords for each char in di
        row1,col1 = getCoords(playfair, di[0])
        row2,col2 = getCoords(playfair, di[1])
        
        #Rule 1
        #if both chars are on the same row of playfair 
        #map each char to the char to its right
        #use % 5 to wrap and stay on the correct row       
        if row1 == row2:
            
            ciphertext.append(playfair[row1][(col1 + 1) % 5])
            ciphertext.append(playfair[row1][(col2 + 1) % 5])		
        
        #Rule 2
        #if both chars are on the same col of playfair 
        #map each char to the char below it
        #use % 5 to wrap and stay on the correct col
        elif col1 == col2:
            
            ciphertext.append(playfair[(row1 + 1) % 5][col1])
            ciphertext.append(playfair[(row2 + 1) % 5][col2])
            
        #Rule 3
        #if rule 1 and 2 fail then the 2 chars are 
        #diagonal to each other
        #switching col1 and col2 will map the correct
        #chars to the chars in the digraph
        else:
            ciphertext.append(playfair[row1][col2])
            ciphertext.append(playfair[row2][col1])
        
    # convert ciphertext into the string ctxt 
    ctxt=""
    for char in ciphertext:
        ctxt += char
    
    return ctxt
    
def decrypt(ctxt, playfair):
    #convert ctxt string into ctxt array holding the digraph pairs
    ctxt = ctxtDigrapher(ctxt)
    plaintext=[]
    
    #for each digraph in ctxt    
    for di in ctxt:
        #extract the row and col coords for each char in di
        row1,col1 = getCoords(playfair, di[0])
        row2,col2 = getCoords(playfair, di[1])

        #Reverse Rule 1
        #if both chars are on the same row of playfair 
        #map each char to the char to its left
        #use % 5 to wrap and stay on the correct row        
        if row1==row2:
            
            plaintext.append(playfair[row1][(col1 - 1) % 5])
            plaintext.append(playfair[row1][(col2 - 1) % 5])

        #Reverse Rule 2
        #if both chars are on the same col of playfair 
        #map each char to the char above it
        #use % 5 to wrap and stay on the correct col        
        elif col1==col2:
            
            plaintext.append(playfair[(row1-1) % 5][col1])
            plaintext.append(playfair[(row2-1) % 5][col2])

        #Rule 3
        #if rule 1 and 2 fail then the 2 chars are 
        #diagonal to each other
        #switching col1 and col2 will map the correct
        #chars to the chars in the digraph        
        else:
            
            plaintext.append(playfair[row1][col2])
            plaintext.append(playfair[row2][col1])

    # Remove any X in plaintext from cleanString or 
    # ptxtDigrapher
    for clean in range(len(plaintext)):
        if "X" in plaintext:
            plaintext.remove("X")

    # convert plaintext into the string ptxt 
    ptxt=""
    for char in plaintext:
        ptxt += char
    
    return ptxt
    

###########################################################################
#Start of Playfair Encryption Tool
progStatus = '0'

print ("Playfair Encryption Tool")
print ("Written By: Taylor Murphy")

while progStatus != '3':
    print ("********************************************************")
    print ("1. Encipher")
    print ("2. Decipher")
    print ("3. Quit")    
        
    progStatus = input("Please select from the options above: ")
    print ("********************************************************")    
    
    if progStatus == '1':
        
        print ("Please enter the key")
        key = input("Key:  ")
        print ('\n')
        print ("Please enter the message")
        ptxt = input("Message:  ")
               
        #prepare ptxt for encryption
        ptxt = cleanString(ptxt)
                        
        #create playfair matrix using key
        playfair = generateSquare(key)
        
        print('\n')
        # encrypt ptxt using playfair and set it equal to ctxt         
        ctxt = encrypt(ptxt, playfair)
        print("Your encrypted message is as follows: ")        
        print(ctxt)        

    if progStatus == '2':
        
        print ("Please enter the key: ")
        key = input("Key:  ")
        print('\n')
        print ("Please enter the ciphertext")
        ctxt = input("Ciphertext:  ")
        
        #create playfair matrix using key        
        playFair = generateSquare(key)
        
        print('\n')        
        # decrypt ctxt using playfair and set it equal to ptxt        
        ptxt = decrypt(ctxt, playFair)
        print("Your decrypted message is as follows: ")        
        print(ptxt) 
    
    if progStatus == '3':
        #exit program
        print ("Exiting Playfair Encryption Tool, Goodbye")
    
       



