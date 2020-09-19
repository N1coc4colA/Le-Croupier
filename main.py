#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:31:54 2020
@author: @n1coc4cola and @teavanui
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
        print("Vous avez perdu votre mise, essayez encore, la chance vous sourira peut-être!")
    if variables.argent <= 0:
        variables.lose = True
        print("Pas de retour en arrière pour vous, vous avez TOUT perdu!! Peut-être que vous reviendrez perdre plus de sous!")

def getMise():
    tmpmise = input("Entrez la valeur de votre mise: ")
    if str(tmpmise).isdigit():
        if int(tmpmise)>0:
            if variables.argent>=int(tmpmise):
                return int(tmpmise)
            else:
                print("N'ayez pas les yeux plus gros que le ventre!")
                return getMise()
        else:
            print("Ne voyez pas négatif! vous n'avez pas encore perdu!")
            return getMise()
    else:
        print("Une nombre entier, pas de virgules ou de lettres enfin!")
        return getMise()

def getNumero():
    tmpnumero = input("Choisissez un nombre entre 1 et 50! ")
    if str(tmpnumero).isdigit():
        if int(tmpnumero)<51 and int(tmpnumero)>0:
            return int(tmpnumero)
        else:
            print("J'ai dit entre 1 et 50, que faites-vous?")
            return getNumero()

def getValues():
    variables.mise = getMise()
    variables.numero = getNumero()
    print("Sam: vous avez misé: ", variables.mise, "sur le numéro ", variables.numero, ". Je lance la roulette!")

def askContinue():
    c=input("Voulez-vous continuer, ou avoir de l'aide? [O/N/H]")
    if c == "o" or c == "O":
        return True
    elif c == "n" or c == "N":
        return False
    elif c == "h" or c == "H":
        variables.helpme()
        return askContinue()
    else:
        print("Hey! Ne vous endormez pas, l'argent n'attend pas!")
        return askContinue()

def showValues(firstTime = False):
    print("Sam: Pour l'instant vous avez: ", variables.argent, "XPF");
    if variables.isFirstTime == False:
        print("Votre dernière mise était de: ", variables.mise, "XPF")
    else:
        variables.isFirstTime = False

def main():
    variables.helpme()
    while variables.wantsToContinue == True and variables.lose == False:
        showValues()
        if askContinue() == True:
            getValues()
            roulette()
        else:
            variables.wantsToContinue = False
    print("Sam: Au plaisir de vous revoir dans notre casino!")

main()
