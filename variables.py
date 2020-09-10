#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:13:53 2020

@author: nicolas
"""

mise=0
argent=5000
numero=0
wantsToContinue=True
isFirstTime=True

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
