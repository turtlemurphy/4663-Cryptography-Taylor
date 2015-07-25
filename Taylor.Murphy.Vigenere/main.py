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

symbols = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode", dest = "mode", default = "encrypt", help = "Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest = "inputFile", help = "Input Name")
    parser.add_argument("-o", "--outputfile", dest = "outputFile", help = "Output Name")
    parser.add_argument("-s", "--seed", dest = "seed", help = "Integer Seed")

    args = parser.parse_args()

    f = open(args.inputFile,'r')
    message = f.read()
    
    if(args.type == 'encrypt'):
        data = rv.encrypt(message,args.mode,args.seed)
        
    else:
        data = rv.decrypt(message,args.mode,args.seed)
        
    o = open(args.outputFile,'w')
    o.write(str(data))


if __name__ == '__main__':
    
    main()
    
    Tableau = open('tableau.txt', 'w')

    vigenere = rv.buildVigenere(symbols)

    for letter in vigenere:
        Tableau.write("%s\n" % letter)
    
    seed = 7487383487438734

    random.seed(7487383487438734)

    keyWord = rv.keywordFromSeed(seed)

    print(keyWord)    
    
    main()