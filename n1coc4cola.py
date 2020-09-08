#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:31:54 2020

@author: @n1coc4cola
"""

mise=0
argent=5000
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
    helpme()
    showValues(True)
    
main()
