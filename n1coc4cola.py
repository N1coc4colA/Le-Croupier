#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:31:54 2020

@author: @n1coc4cola
"""

mise=0
argent=5000

    
def getValues():
    m=input("Quelle somme souhaitez vous miser? Entrez la valeur: ")
    mise=int(m)
    print("Sam: vous avez misé: ", mise, ", Je lance la roulette!")
    """roulette() exec func"""


def askContinue():
    c=input("Voulez-vous continuer? [O/N]")
    if (c[0] == ("o" or "O")):
        getValues()
    elif(c[0] == ("n" or "N")):
        print("Sam: Au plaisir de vous revoir dans notre casino!")
    else:
        print("Hey! Ne vous endormez pas, l'argent n'attend pas!")
        askContinue()


def showValues(firstTime = False):
    print("Sam: Pour l'instant vous avez: ", argent);
    if firstTime == False:
        print("Votre dernière mise était de: ", mise)
    askContinue()

def main():
    """helpme() exec func"""
    showValues(True)
    
main()