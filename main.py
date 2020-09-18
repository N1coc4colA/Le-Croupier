#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:31:54 2020
@author: @n1coc4cola
"""

import variables
import math
from random import randrange

def roulette():
    num = randrange(0, 50, 1)+1
    print("Le numéro sorti est le ", num)
    if (num == variables.numero):
        variables.argent+=mise*3
    elif (num%2 == variables.numero%2):
        variables.argent+=math.ceil(variables.mise*0.5)
        print("Vous avez gagné ", math.ceil(variables.mise*0.5), ", vous ferez mieux la prochaine fois!")
    else:
        variables.argent-=variables.mise
        print("Vous avez perdu, essayez encore, la chance vous sourira peut-être!")

    
def getValues():
    """Use .isDigit() to check that it is only numbers"""
    tmpmise=input("Entrez votre valeur")
    if tmpmise.isDigit():
        if variables.argent>=tmpmise and tmpmise>0:
            variables.mise=int(tmpmise)
        else:
            getValues()
            
            
    else:
        getValues()
    tmpnumero=input("Sur quel numéro voulez-vous miser ? Entrez le numéro en question : ")
    if tmpnumero.isDigit():
        variables.mise=int(tmpnumero)
    else:
        getValues()
    variables.mise = int(input("Quelle somme souhaitez vous miser? Entrez la valeur: "))
    variables.numero = int(input("Vous voulez miser sur quel numéro? De 1 à 50!"))
    print("Sam: vous avez misé: ", variables.mise, "sur le numéro ", variables.numero, ". Je lance la roulette!")
    """When we'll use digit checks, leave it here will be useful."""
    roulette()


def askContinue():
    c=input("Voulez-vous continuer? [O/N]")
    if (c[0] == ("o" or "O")):
        return True
    elif(c[0] == ("n" or "N")):
        return False
    else:
        print("Hey! Ne vous endormez pas, l'argent n'attend pas!")
        return askContinue()


def showValues(firstTime = False):
    print("Sam: Pour l'instant vous avez: ", variables.argent, "XPF");
    if variables.isFirstTime == False:
        print("Votre dernière mise était de: ", variables.mise, "XPF")

def main():
    variables.helpme()
    while variables.wantsToContinue == True:
        showValues()
        if askContinue() == True:
            getValues()
        else:
            variables.wantsToContinue = False
    print("Sam: Au plaisir de vous revoir dans notre casino!")
    
main()
