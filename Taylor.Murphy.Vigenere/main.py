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

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode", dest = "mode", default = "encrypt", help = "Enter: encrypt or decrypt")
    parser.add_argument("-s", "--seed", dest = "seed", default = 77065084072073083070085078, help = "Enter an integer seed value")
    parser.add_argument("-i", "--inputfile", dest = "inputFile", help = "Enter the full input filename")
    parser.add_argument("-o", "--outputfile", dest = "outputFile", help = "Enter the full output filename")
    
    args = parser.parse_args()

    print ("Vigenère Encryption Tool")
    print ("Written By: Taylor Murphy")
    print ("********************************************************")
    
    random.seed(args.seed)
    keyWord = rv.keywordFromSeed(args.seed)

    inp1 = open(args.inputFile,'r')
    message = inp1.read()
    
    inp2 = open(args.inputFile,'r')
    ctxt = inp2.read()
    
    print("Keyword:     ", keyWord)
    print("Message:     ", message)
    
    if(args.mode == 'encrypt'):
        rv.encrypt(message, keyWord)
        
    else:
        rv.decrypt(ctxt, keyWord)
    
    print ("Exiting Vigenère Encryption Tool, Goodbye")
    print ("********************************************************")


if __name__ == '__main__':
    
    #Use this as a template for the testing block
    #python3 main.py -m encrypt -s 7487383487438734 -i plainText.txt -o encryptedText.txt 
    #python3 main.py -m decrypt -s 7487383487438734 -i encryptedText.txt -o decryptedText.txt
    
    main()
    
#    keyWord = rv.keywordFromSeed(77065084072073083070085078)
#    
#    inp1 = open('plainText.txt','r')
#    message = inp1.read()    
#    
#    rv.encrypt(message, keyWord)
    
    
    
    
    
    
    
    
    
    
    
    