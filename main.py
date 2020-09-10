#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:31:54 2020
@author: @n1coc4cola
"""

import storage
import math
from random import randrange


def helpme():
    print("Nous allons vous expliquer les règles!")
    print("Nous allons jouer à la roulette\n")
    print("La roulette est composée de 50 cases, des cases numérotées de 0 à 49 et de couleurs rouges et noires")
    print("Les cases noires seront les cases paires et les cases rouges seront les cases impaires\n")
    print("Je vais faire tourner la roulette avec une seule bille, si la bille tombe sur le numéro que vous avez misé,")
    print("Vous gagnez le triple de votre mise, mais si ce n'est pas le cas,")
    print("Nous allons regarder si la bille tombe sur la couleur que vous avez misée, et si c'est le cas,")
    print("Uniquement la moitié de votre mise vous sera rendu, en cas contraire vous la perdez\n")
    print("Les présentations du jeu sont faites, nous pouvons jouer")


def roulette():
    num = randrange(0, 50, 1)+1
    print("Le numéro sorti est le ", num)
    if (num == storage.numero):
        storage.argent+=mise*3
    elif (num%2 == storage.numero%2):
        storage.argent+=math.ceil(storage.mise*0.5)
        print("Vous avez gagné ", math.ceil(storage.mise*0.5), ", vous ferez mieux la prochaine fois!")
    else:
        storage.argent-=storage.mise
        print("Vous avez perdu, essayez encore, la chance vous sourira peut-être!")


def getMise():
    m = input("Quelle somme souhaitez vous miser? Entrez la valeur: ")
    print(m.isdigit())
    if str(m).isdigit() == True:
        if int(m) <= storage.argent:
            storage.mise = int(m)
        else:
            print("Sarah: Oh! N'abusez pas non plus, ce n'est pas une banque ici!")
            getMise()
    else:
        print("Ne faites pas l'andouille, on sais tous les deux qu'il n'y a pas que des chiffres!")
        getMise()


def getNumber():
    n = input("Vous voulez miser sur quel numéro? De 1 à 50!")
    if str(n).isdigit() == True:
        if (int(n)>50):
            print("Vous ne voulez plus jouer?? Moi oui, alors donnez-moi un chiffre, vous avez déjà fait votre mise.")
            getNumber()
        else:
            storage.numero = int(n)
            print("Sam: vous avez misé: ", storage.mise, "sur le numéro ", storage.numero, ". Je lance la roulette!")
            roulette()
    else:
        print("Oh, arrêtez ou j'appel la sécu! L'alcool est mauvais pour la santé et votre bourse apparemment...")
        getNumber()


def getValues():
    getMise()
    getNumber()


def askContinue():
    c=input("Voulez-vous continuer ou avoir de l'aide? [O/N/H]")
    if (c[0] == ("o" or "O")):
        return True
    elif(c[0] == ("n" or "N")):
        return False
    elif(c[0] == ("h" or "H")):
        helpme()
        return askContinue()
    else:
        print("Hey! Ne vous endormez pas, l'argent n'attend pas!")
        return askContinue()


def showValues(firstTime = False):
    print("Sam: Pour l'instant vous avez: ", storage.argent, "XPF");
    if storage.isFirstTime == False:
        print("Votre dernière mise était de: ", storage.mise, "XPF")


def main():
    helpme()
    while storage.wantsToContinue == True:
        showValues()
        if askContinue() == True:
            getValues()
        else:
            storage.wantsToContinue = False
    print("Sam: Au plaisir de vous revoir dans notre casino!")


main()
