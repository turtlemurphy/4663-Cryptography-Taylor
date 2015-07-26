###############################################
# Name: Taylor Murphy
# Class: CMPS 4663 Cryptography
# Date: 25 July 2015
# Program 2 - Randomized Vigenère Cipher
###############################################

import random
import argparse
import sys
import randomized_vigenere as rv


symbols = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
#symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

#def main():
#    parser = argparse.ArgumentParser()
#
#    parser.add_argument("-m", "--mode", dest = "mode", default = "encrypt", help = "Enter: encrypt or decrypt")
#    parser.add_argument("-s", "--seed", dest = "seed", help = "Enter an integer seed value")
#    parser.add_argument("-i", "--inputfile", dest = "inputFile", help = "Enter the full input filename")
#    parser.add_argument("-o", "--outputfile", dest = "outputFile", help = "Enter the full output filename")
#    
#    args = parser.parse_args()
#
#    inp = open(args.inputFile,'r')
#    message = inp.read()
#    
#    if(args.type == 'encrypt'):
#        data = rv.encrypt(message, args.mode, args.seed)
#        
#    else:
#        data = rv.decrypt(message, args.mode, args.seed)
#        
#    out = open(args.outputFile,'w')
#    out.write(str(data))


if __name__ == '__main__':
    
    #Use this as a template for the testing block
    #python3 main.py -m encrypt -s 7487383487438734 -i plainText.txt -o encryptedText.txt 
    #python3 main.py -m decrypt -s 7487383487438734 -i encryptedText.txt -o decryptedText.txt
    
    #Testing Block
    #############################################
    progStatus = '1'
    print ("Vigenère Encryption Tool")
    print ("Written By: Taylor Murphy")

    while progStatus != '3':
        print ("********************************************************")
        print ("1. Encrypt")
        print ("2. Decrypt")
        print ("3. Quit")    
        
        progStatus = input("Please select from the options above: ")
        print ("********************************************************")    
    
        if progStatus == '1':
            inp = open('plainText.txt','r')
            message = inp.read()
            
            seed = 12001907
#            print ("Please enter the seed")
#            seed = input("Seed: ")
#            seed = int(seed)
            random.seed(seed)
            
            temp = (seed % 100)
            temp = chr(temp)
            seed = seed // 100
            
            print (temp)
            print (seed)
            
            #Extracts text version of the keyWord    
            #keyWord = rv.keywordFromSeed(seed)
            #print("The keyword is: ", keyWord)
            
            vigenere = rv.buildVigenere(symbols)
            
            progStatus = '3'
                
        if progStatus == '2':
            pass
        
        if progStatus == '3':
            #exit program
            print ("Exiting Vigenère Encryption Tool, Goodbye")
    
    #############################################
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    