#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:36:46 2024

@author: camelia
"""

import numpy as np

def afficher (p) :
    """ afficher(p)
    @ p : liste des différents coeff de la fonction
    chaine de chara
    """
    polynome = ""
    for n in range(1, len(p)) :
        polynome += p[n] + "X^" + "+"
    polynome += p[0]    
    
print(afficher(["1", "6", "9"]))

def get_valeur(p, x) :
    """ get_valeur(p, x)
    @ p : liste des différents coeff de la fonction
    @ x : valeur de la variable
    """
    polynome = 0
    for i in range (0, len(p)):
        polynome += p[i] * x**i
    return polynome

print(get_valeur([1, 3, 5], 2))